# ClassWork 2
# part 1
# Создать класс complex_number. Комплексное число состоит из двух частей: real_part: int, img_part: int.
# Настроить суммирование двух complex_number:
# complex_number(5, 3) + complex_number(1, 1) = complex_number(6, 4)
# Настроить разность двух complex_number:
# complex_number(5, 3) - complex_number(1, 1) = complex_number(4, 2)
# Настроить произведение двух complex_number:
# complex_number(5, 3) * complex_number(1, 1) = complex_number(2, 8)

# part 2
# Создать подкласс weird_complex_number который наследуется от класса complex_number. В дополнение к
# двум частям которые есть у его родителя, у данного класса есть третья часть: abs_part: int.
# Для данного класса, настроить сумму и разность, используя родительские сумму и разность
# При сумме и разности, результату берется abs_part который больше
# weird_complex_number(5, 3, 8) + weird_complex_number(1, 1, 4) = weird_complex_number(6, 4, 8)
# weird_complex_number(5, 3, 2) - weird_complex_number(1, 1, 4) = weird_complex_number(4, 2, 4)


# class ComplexNumber:
#     def __init__(self, real_part: int, img_part: int):
#         self.real_part = real_part
#         self.img_part = img_part
#
#     def __add__(self, other):
#         new_real = self.real_part + other.real_part
#         new_img = self.img_part + other.img_part
#         return ComplexNumber(new_real, new_img)
#
#     def __sub__(self, other):
#         new_real = self.real_part - other.real_part
#         new_img = self.img_part - other.img_part
#         return ComplexNumber(new_real, new_img)
#
#     def __mul__(self, other):
#         new_real = self.real_part * other.real_part - self.img_part * other.img_part
#         new_img = self.real_part * other.img_part + self.img_part * other.real_part
#         return ComplexNumber(new_real, new_img)
#
#     def __str__(self):
#         return str(self.real_part) + '+' + str(self.img_part) + 'i'
#
#
# class WeirdComplexNumber(ComplexNumber):
#     def __init__(self, real_part: int, img_part: int, abs_part: int):
#         super().__init__(real_part, img_part)
#         self.abs_part = abs_part
#
#     def __add__(self, other):
#         two_parts = super().__add__(other)
#         new_abs_part = max(self.abs_part, other.abs_part)
#         return WeirdComplexNumber(two_parts.real_part, two_parts.img_part, new_abs_part)
#
#     def __sub__(self, other):
#         two_parts = super().__sub__(other)
#         new_abs_part = max(self.abs_part, other.abs_part)
#         return WeirdComplexNumber(two_parts.real_part, two_parts.img_part, new_abs_part)
#
#     def __str__(self):
#         return super().__str__() + '+' + str(self.abs_part)
#
#
# num1 = WeirdComplexNumber(5, 3, 8)
# num2 = WeirdComplexNumber(1, 1, 4)
# # print(num1)
# # print(num2)
# num3 = num1 - num2
# print(num3)
# print(type(num3))


# ООП - Объектно Ориентированное Программирование
# Класс - Уникальная структура, которую создает программист


# class Product:  # Компонент - класс, который существует чтобы быть атрибутом другого класса
#     def __init__(self, name: str, price: int):
#         self.name = name
#         self.price = price
#
#
# class Dish:  # Композиция - класс, который среди своих атрибутов принимает объекты других классов
#     def __init__(self, name: str, products: list):
#         self.name = name
#         self.products = products
#
#     def getPrice(self):
#         final_price = 0
#         for i in range(0, len(self.products), 1):
#             final_price += self.products[i].price
#         return final_price
#
#
# product1 = Product('Potato', 200)
# product2 = Product('Milk', 450)
# product3 = Product('Butter', 500)
# dish1 = Dish('Mashed_Potatoes', [product1, product2, product3])
# print(dish1.getPrice())


# class Student:
#     def __init__(self):
#         pass


# class Worker:
#     def __init__(self):
#         pass


# class Children:
#     def __init__(self):
#         pass


# class Society:
#     def __init__(self, peoples: list):
#         self.people = peoples

#     def getCountStudents(self):
#         pass

#     def getCountWorkers(self):
#         pass

#     def getCountChild(self):
#         pass

# class Society:
#     def __init__(self, peoples: list):
#         self.peoples = peoples

#     def getCountStudents(self):
#         # Возвращает кол-во объектов класса Student в списке self.people
#         counter = 0
#         for i in range(0, len(self.peoples), 1):
#             if type(self.peoples[i]) == Student:
#                 counter += 1
#         return counter

#     def getCountWorkers(self):
#         # Возвращает кол-во объектов класса Worker в списке self.people
#         counter = 0
#         for i in range(0, len(self.peoples), 1):
#             if isinstance(self.peoples[i], Worker):
#                 counter += 1
#         return counter

#     def getCountChild(self):
#         # Возвращает кол-во объектов класса Children в списке self.people
#         counter = 0
#         for i in range(0, len(self.peoples), 1):
#             if type(self.peoples[i]) is Children:
#                 counter += 1
#         return counter