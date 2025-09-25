



# Boolean

# Что напечатает код?
print(10 > 9)
print(10 == 9)
print(10 < 9)

# Заверши условие, чтобы выводился True
x = 15
print(x > 10)


# Operators

# Используя оператор сложения, посчитай:
a = 10
b = 5
print(a + b)

# Используя оператор and, сделай проверку:
x = 7
print(x > 5 and x < 10)


# 3. Lists

# Создай список из фруктов и выведи второй элемент
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

# Добавь новый элемент "orange" в список
fruits.append("orange")
print(fruits)

# Пройди по списку и выведи каждый элемент
for f in fruits:
    print(f)


# 4. Tuples

# Создай кортеж из 3 чисел и выведи последний элемент
numbers = (1, 2, 3)
print(numbers[-1])

# Преобразуй кортеж в список и обратно
num_list = list(numbers)
num_list.append(4)
numbers = tuple(num_list)
print(numbers)


# 5. Sets

# Создай множество из чисел и добавь элемент 10
myset = {1, 2, 3, 4, 5}
myset.add(10)
print(myset)

# Удали элемент 3 из множества
myset.remove(3)
print(myset)


# 6. Dictionaries

# Создай словарь и выведи значение по ключу "name"
person = {"name": "Ali", "age": 18}
print(person["name"])

# Добавь новый ключ "country": "Kazakhstan"
person["country"] = "Kazakhstan"
print(person)

# Пройди по словарю и выведи все ключи
for key in person:
    print(key)


# 7. if...else

# Проверка возраста
age = 20
if age < 18:
    print("Too young")
else:
    print("Welcome")

# Проверка четности
num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# 8. match (Python 3.10+)

# День недели по номеру
day = 3
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")


# 9. while loop

# Выведи числа от 1 до 5
i = 1
while i <= 5:
    print(i)
    i += 1

# Сумма чисел от 1 до 100
i = 1
total = 0
while i <= 100:
    total += i
    i += 1
print("Sum =", total)


# 10. for loop

# Пройди по списку фруктов
for f in fruits:
    print(f)

# Выведи буквы слова "Python"
for ch in "Python":
    print(ch)

# Посчитай сумму чисел в списке
numbers = [2, 4, 6, 8, 10]
total = 0
for n in numbers:
    total += n
print("Sum =", total)
