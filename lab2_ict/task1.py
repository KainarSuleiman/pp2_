# Step 1: Define functions for basic operations
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:  # Avoid division by zero
        return a / b
    else:
        return "Error! Division by zero."


# Step 2: Main program
def calculator():
    print("Welcome to the Calculator!")

    # Step 3: Get user input
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Choose operation (add, subtract, multiply, divide): ").strip().lower()

    # Step 4: Perform operation and display the result
    if operation == "add":
        print("Result:", add(num1, num2))
    elif operation == "subtract":
        print("Result:", subtract(num1, num2))
    elif operation == "multiply":
        print("Result:", multiply(num1, num2))
    elif operation == "divide":
        print("Result:", divide(num1, num2))
    else:
        print("Invalid operation!")


# Call the calculator function
calculator()
