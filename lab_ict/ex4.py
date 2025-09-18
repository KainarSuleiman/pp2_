

numbers = list(range(1,51))
filtered_list = []
for number in numbers:
    if number % 3 == 0 and number % 5 == 0:
        filtered_list.append(number)
print(filtered_list)