# Original Code
# number = int(input("Enter a number: "))
# result = 1
# for i in range(1, number + 1):
#     result *= i
# print(f"Factorial of {number} is {result}")


# Step 1: Define a function to calculate factorial
def calculate_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Step 2: Main program
def main():
    number = int(input("Enter a number: "))
    factorial = calculate_factorial(number)
    print(f"Factorial of {number} is {factorial}")

# Call the main function
main()
