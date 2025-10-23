

def cube_of_numbers(n):
    for i in range(1, n+1):
        yield i**3


n = int(input("Enter a number: "))
for c3 in cube_of_numbers(n):
    print(c3)


