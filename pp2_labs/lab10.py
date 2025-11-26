# phonebook_and_snake_db.py
import os
import csv
import json
import psycopg2
from psycopg2.extras import RealDictCursor, Json
from datetime import datetime

# --------------------------
# Подключение к PostgreSQL
# --------------------------

def get_conn():
    return psycopg2.connect(
        host=os.getenv("PGHOST", "localhost"),
        port=os.getenv("PGPORT", 5432),
        user=os.getenv("PGUSER", "postgres"),
        password=os.getenv("PGPASSWORD", "Kayneke23"),
        dbname=os.getenv("PGDATABASE", "postgres")
    )

# ============================================================
#                   СОЗДАНИЕ ТАБЛИЦ
# ============================================================

def create_tables():
    ddl = """
    CREATE TABLE IF NOT EXISTS phonebook_users (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(100) NOT NULL,
        last_name VARCHAR(100),
        phone VARCHAR(30) UNIQUE NOT NULL,
        email VARCHAR(255),
        created_at TIMESTAMP DEFAULT now()
    );

    CREATE TABLE IF NOT EXISTS snake_users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        created_at TIMESTAMP DEFAULT now()
    );

    CREATE TABLE IF NOT EXISTS snake_levels (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        speed INTEGER NOT NULL,
        walls_config JSONB,
        description TEXT
    );

    CREATE TABLE IF NOT EXISTS snake_user_scores (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES snake_users(id) ON DELETE CASCADE,
        score INTEGER NOT NULL,
        level_id INTEGER REFERENCES snake_levels(id),
        state JSONB,
        saved_at TIMESTAMP DEFAULT now()
    );
    """
    conn = get_conn()
    with conn:
        with conn.cursor() as cur:
            cur.execute(ddl)
    conn.close()
    print("Таблицы успешно созданы!")

# ============================================================
#              PHONEBOOK: вставка данных из CSV
# ============================================================

def insert_from_csv(csv_path):
    conn = get_conn()
    inserted = 0
    with conn:
        with conn.cursor() as cur:
            with open(csv_path, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    first_name = row.get("first_name", "").strip()
                    phone = row.get("phone", "").strip()

                    if not first_name or not phone:
                        print("Пропущена строка:", row)
                        continue

                    cur.execute("""
                        INSERT INTO phonebook_users (first_name, last_name, phone, email)
                        VALUES (%s, %s, %s, %s)
                        ON CONFLICT (phone) DO UPDATE
                        SET first_name = EXCLUDED.first_name,
                            last_name = EXCLUDED.last_name,
                            email = EXCLUDED.email
                    """, (
                        row.get("first_name"),
                        row.get("last_name"),
                        row.get("phone"),
                        row.get("email")
                    ))
                    inserted += 1
    conn.close()
    print(f"Загружено строк: {inserted}")

# ============================================================
#      PHONEBOOK: вставка данных через консоль
# ============================================================

def insert_from_console():
    print("Оставь имя пустым, чтобы остановить ввод.")
    while True:
        first_name = input("Имя: ").strip()
        if not first_name:
            break

        last_name = input("Фамилия: ").strip() or None
        phone = input("Телефон: ").strip()
        email = input("Email: ").strip() or None

        conn = get_conn()
        with conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO phonebook_users (first_name, last_name, phone, email)
                    VALUES (%s, %s, %s, %s)
                    ON CONFLICT (phone) DO UPDATE
                    SET first_name = EXCLUDED.first_name,
                        last_name = EXCLUDED.last_name,
                        email = EXCLUDED.email
                """, (first_name, last_name, phone, email))
        conn.close()
        print("Сохранено!")

# ============================================================
#                 PHONEBOOK: обновление данных
# ============================================================

def update_contact(old_phone, new_first=None, new_phone=None):
    conn = get_conn()
    set_parts = []
    params = []

    if new_first:
        set_parts.append("first_name=%s")
        params.append(new_first)
    if new_phone:
        set_parts.append("phone=%s")
        params.append(new_phone)

    params.append(old_phone)

    sql = "UPDATE phonebook_users SET " + ", ".join(set_parts) + " WHERE phone=%s"

    with conn:
        with conn.cursor() as cur:
            cur.execute(sql, tuple(params))
            print("Обновлено строк:", cur.rowcount)
    conn.close()

# ============================================================
#                 PHONEBOOK: выборка данных
# ============================================================

def query_contacts(name_like=None, phone_like=None):
    conn = get_conn()
    sql = "SELECT * FROM phonebook_users WHERE 1=1"
    params = []

    if name_like:
        sql += " AND first_name ILIKE %s"
        params.append(f"%{name_like}%")

    if phone_like:
        sql += " AND phone ILIKE %s"
        params.append(f"%{phone_like}%")

    with conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(sql, tuple(params))
            rows = cur.fetchall()
            return rows

# ============================================================
#                 PHONEBOOK: удаление
# ============================================================

def delete_contact(first_name=None, phone=None):
    conn = get_conn()
    sql = "DELETE FROM phonebook_users WHERE first_name=%s OR phone=%s"
    with conn:
        with conn.cursor() as cur:
            cur.execute(sql, (first_name, phone))
            print("Удалено:", cur.rowcount)
    conn.close()

# ============================================================
#           ЗМЕЙКА: регистрация / получение уровня
# ============================================================

def ensure_user(username):
    conn = get_conn()
    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id FROM snake_users WHERE username=%s", (username,))
            row = cur.fetchone()
            if row:
                print("Пользователь найден!")
                return row[0]
            cur.execute("INSERT INTO snake_users (username) VALUES (%s) RETURNING id", (username,))
            uid = cur.fetchone()[0]
            print("Создан новый пользователь!")
            return uid

# Последний уровень
def get_last_user_score(user_id):
    conn = get_conn()
    with conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("""
                SELECT s.*, l.name AS level_name, l.speed AS level_speed
                FROM snake_user_scores s
                LEFT JOIN snake_levels l ON l.id = s.level_id
                WHERE user_id=%s
                ORDER BY saved_at DESC
                LIMIT 1
            """, (user_id,))
            return cur.fetchone()

# ============================================================
#           ЗМЕЙКА: сохранение состояния игры
# ============================================================

def save_game_state(user_id, score, level_id, state):
    conn = get_conn()
    with conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO snake_user_scores (user_id, score, level_id, state)
                VALUES (%s, %s, %s, %s)
            """, (user_id, score, level_id, Json(state)))
    conn.close()
    print("Прогресс сохранён!")

# ============================================================
#               Пример работы (меню)
# ============================================================

if __name__ == "__main__":
    print("1 — создать таблицы")
    print("2 — загрузить CSV в PhoneBook")
    print("3 — вводить контакты вручную")
    print("4 — обновить контакт")
    print("5 — запросить контакты")
    print("6 — удалить контакт")
    print("7 — демо для Змейки")
    choice = input("Выбери: ")

    if choice == "1":
        create_tables()

    elif choice == "2":
        path = input("Путь до CSV: ")
        insert_from_csv(path)

    elif choice == "3":
        insert_from_console()

    elif choice == "4":
        old = input("Старый телефон: ")
        new_first = input("Новое имя: ") or None
        new_phone = input("Новый телефон: ") or None
        update_contact(old, new_first, new_phone)

    elif choice == "5":
        name = input("Имя содержит: ")
        print(query_contacts(name_like=name))

    elif choice == "6":
        name = input("Имя: ")
        phone = input("Телефон: ")
        delete_contact(name, phone)

    elif choice == "7":
        username = input("Имя игрока: ")
        user_id = ensure_user(username)
        last_state = get_last_user_score(user_id)
        print("Последнее сохранение:", last_state)
        print("---- Сохраняем новое состояние ----")
        score = int(input("Введите текущий счёт: "))
        level = int(input("ID уровня: "))
        state = {"snake": [[5,5],[5,6]], "direction": "UP"}
        save_game_state(user_id, score, level, state)
