#
#
#
#
#
# from functools import reduce
#
# nums = [2, 3, 4, 5]
# result = reduce(lambda x, y: x * y, nums)
# print("Product of all nums:", result)
#
#
#
# text = input("Enter a string: ")
#
# upper_case = sum(1 for bukvy in text if bukvy.isupper())
# lower_case = sum(1 for bukvy in text if bukvy.islower())
#
# print("Uppercase letters:", upper_case)
# print("Lowercase letters:", lower_case)
#
#
#
# text = input("Enter a string: ")
#
# if text == text[::-1]:
#     print("It is a palindrome.")
# else:
#     print("It is not a palindrome.")
#
#     word = 'ABABA'
#     flag = True
#     for i in range(0, len(word) // 2, 1):
#         if word[i] != word[-i - 1]:
#             flag = False
#             break
#     print(flag)
#
#
# import time
# import math
#
# num = int(input("Enter a number: "))
# milli = int(input("Enter milliseconds: "))
#
# time.sleep(milli / 1000)
# result = math.sqrt(num)
#
# print(f"Square root of {num} after {milli} miliseconds is {result}")
#
#
# t = (True, 0 , 23, "Kainar")
#
# print(all(t))


word = input('Enter a word: ')

cifra = sum(1 for c in word if c.isdigit())
bukvy = sum(1 for b in word if b.isalpha() )

print(bukvy)
print(cifra)









