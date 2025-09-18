

try:
    number = int(input("Введите число для таблицы умножения: "))
    if number > 0:
        print(f"Таблица умножения для {number}:")
        for i in range(1, 11):
            print(f"{number} x {i} = {number * i}")
    else:
        print("Ошибка: Введите положительное число.")
except ValueError:
    print("Ошибка: Введите целое число.")