

spisok = []



while True:
    print("\nspisok:")
    print("1. Добавить задачу")
    print("2. Показать все задачи")
    print("3. Удалить задачу по номеру")
    print("q. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        task = input("Введите задачу: ")
        spisok.append(task)
        print(f'Задача "{task}" добавлена.')
    elif choice == "2":
        if spisok:
            print("Список задач:")
            for idx, task in enumerate(spisok, 1):
                print(f"{idx}. {task}")
        else:
            print("Список задач пуст.")
    elif choice == "3":
        try:
            task_num = int(input("Введите номер задачи для удаления: "))
            if 1 <= task_num <= len(spisok):
                removed_task = spisok.pop(task_num - 1)
                print(f'Задача "{removed_task}" удалена.')
            else:
                print("Неверный номер задачи.")
        except ValueError:
            print("Ошибка: введите корректный номер.")
    elif choice == "q":
        print("Выход из программы.")
        break
    else:
        print("Некорректный ввод. Пожалуйста, выберите допустимое действие.")
