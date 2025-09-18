
contact_book = {}

while True:
    print("\nContact Book Manager:")
    print("1. Добавить новый контакт")
    print("2. Показать все контакты")
    print("3. Найти контакт по имени")
    print("4. Удалить контакт")
    print("q. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        name = input("Введите имя контакта: ")
        if name in contact_book:
            print(f"Контакт с именем '{name}' уже существует.")
        else:
            phone = input("Введите номер телефона: ")
            contact_book[name] = phone
            print(f"Контакт '{name}' добавлен.")

    elif choice == "2":
        if contact_book:
            print("Контакты:")
            for name, phone in contact_book.items():
                print(f"{name}: {phone}")
        else:
            print("Телефонная книга пуста.")

    elif choice == "3":
        name = input("Введите имя для поиска: ")
        if name in contact_book:
            print(f"{name}: {contact_book[name]}")
        else:
            print(f"Контакт с именем '{name}' не найден.")

    elif choice == "4":
        name = input("Введите имя контакта для удаления: ")
        if name in contact_book:
            del contact_book[name]
            print(f"Контакт '{name}' удален.")
        else:
            print(f"Контакт с именем '{name}' не найден.")

    elif choice == "q":
        print("Выход из программы.")
        break

    else:
        print("Некорректный ввод. Пожалуйста, выберите допустимое действие.")
