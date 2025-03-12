# Exceptions in Python

# Task 1
try:
    n = float(input("Enter a number: "))
    print(f"100 divided by {n} is {100 / n}.")
except ZeroDivisionError:
    print("Oops! You cannot divide by zero.")
except ValueError:
    print("Invalid input! Please enter a valid number.")


# Task 2
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError:
    print("\nIndexError occurred! List index out of range.")

try:
    my_dict = {"name": "John", "age": 26}
    print(my_dict["address"])
except KeyError:
    print("KeyError occurred! Key not found in the dictionary.")

try:
    test = "Hello" + 5
except TypeError:
    print("TypeError occurred! Unsupported operand types.")


# Task 3
try:
    n1 = float(input("\nEnter the first number: "))
    n2 = float(input("Enter the second number: "))

    # Try to divide the first number by the second number
    result = n1 / n2

except ZeroDivisionError:
    print("Oops! You cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter valid numbers.")
else:
    print(f"The result is {result}.")
finally:
    print("This block always executes.")
