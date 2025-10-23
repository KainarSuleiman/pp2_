

## 1
#
# class StringHandler:
#     def __init__(self):
#         self.s = ""
#
#     def getString(self):
#         self.s = input("Enter a string: ")
#
#     def printString(self):
#         print(self.s.upper())


# 2

#
# class Shape:
#     def area(self):
#         return 0
#
# class Square(Shape):
#     def __init__(self, length):
#         self.length = length
#
#     def area(self):
#         return self.length * self.length


# 3
#
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width

# 4
#
# import math
#
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def show(self):
#         print(f"Point({self.x}, {self.y})")
#
#     def move(self, x, y):
#         self.x = x
#         self.y = y
#
#     def dist(self, other_point):
#         return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)


# 5

# class Account:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited {amount}. New balance = {self.balance}")
#
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient funds!")
#         else:
#             self.balance -= amount
#             print(f"Withdrew {amount}. New balance = {self.balance}")



# 6

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 11, 13, 16, 18, 19]
# primes = list(filter(lambda x: is_prime(x), numbers))
# print("Prime numbers:", primes)

## function


# 1
#
# def grams_to_ounces(grams):
#     return 28.3495231 * grams


# 2

# def fahrenheit_to_centigrade(f):
#     return (5 / 9) * (f - 32)

# 3

# def solve(numheads, numlegs):
#     for chickens in range(numheads + 1):
#         rabbits = numheads - chickens
#         if 2*chickens + 4*rabbits == numlegs:
#             return chickens, rabbits
#


# 4


# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True
#
# def filter_prime(numbers):
#     return [n for n in numbers if is_prime(n)]


# 5

# import itertools
#
# def string_permutations(s):
#     perms = itertools.permutations(s)
#     for p in perms:
#         print("".join(p))


# 6
#
# def reverse_words(sentence):
#     words = sentence.split()
#     return " ".join(words[::-1])


# 7

# def has_33(nums):
#     for i in range(len(nums)-1):
#         if nums[i] == 3 and nums[i+1] == 3:
#             return True
#     return False

# 8

# def spy_game(nums):
#     code = [0, 0, 7]
#     for n in nums:
#         if n == code[0]:
#             code.pop(0)
#         if not code:
#             return True
#     return False


# 9

#
# import math
#
# def sphere_volume(r):
#     return (4/3) * math.pi * (r**3)

# 10

# def unique_list(lst):
#     result = []
#     for x in lst:
#         if x not in result:
#             result.append(x)
#     return result

# 11

#
# def is_palindrome(s):
#     s = s.replace(" ", "").lower()
#     return s == s[::-1]

# 12

# def histogram(lst):
#     for n in lst:
#         print("*" * n)

# 13

#
# import random
#
# def guess_game():
#     print("Hello! What is your name?")
#     name = input()
#
#     print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
#     number = random.randint(1, 20)
#     guesses = 0
#
#     while True:
#         print("Take a guess.")
#         guess = int(input())
#         guesses += 1
#
#         if guess < number:
#             print("Your guess is too low.")
#         elif guess > number:
#             print("Your guess is too high.")
#         else:
#             print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
#             break


# 14

# movies = [
#     {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
#     {"name": "Hitman", "imdb": 6.3, "category": "Action"},
#     {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
#     {"name": "The Help", "imdb": 8.0, "category": "Drama"},
#     {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
#     {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
#     {"name": "Love", "imdb": 6.0, "category": "Romance"},
#     {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
#     {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
#     {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
#     {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
#     {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
#     {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
#     {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
#     {"name": "We Two", "imdb": 7.2, "category": "Romance"}
# ]
#
# # 1. Один фильм > 5.5
# def is_above_5_5(movie):
#     return movie["imdb"] > 5.5
#
# # 2. Список фильмов > 5.5
# def filter_movies_above_5_5(movies):
#     return [m for m in movies if m["imdb"] > 5.5]
#
# # 3. Фильмы по категории
# def movies_by_category(movies, category):
#     return [m for m in movies if m["category"] == category]
#
# # 4. Средний рейтинг всех фильмов
# def average_imdb(movies):
#     return sum(m["imdb"] for m in movies) / len(movies)
#
# # 5. Средний рейтинг по категории
# def average_imdb_by_category(movies, category):
#     cat_movies = [m["imdb"] for m in movies if m["category"] == category]
#     return sum(cat_movies) / len(cat_movies)
#


#
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.grades = []
#
#
#     def add_grade(self, grade)
#         self.grades.append(grade)

#
# def is_evod(n):
#     if n % 2 == 0:
#         return "It is Even"
#     else:
#         return "It is Odd"
#
# n= int(input("Enter a number: "))
#
# print(is_evod(n))




def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = 10
print(",".join(str(num) for num in even_numbers(n)))
