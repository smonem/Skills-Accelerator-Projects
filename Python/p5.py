# Math Menu
import math


# Test choice validity
def validate_choice(i):
    if not i.isnumeric() or int(i) not in range(1, 4):
        print("Invalid input")
        return False
    return True


# Test number is positive int
def validate_input(i):
    if not i.isnumeric() or int(i) <= 0:
        print("Invalid input")
        return False
    return True


# Recusively calculate factorial
def calc_fact(n):
    if n == 1:
        return n
    return n * calc_fact(n - 1)


# Recusively calculate fib number for position
def calc_fib(n):
    if n <= 1:
        return n
    return calc_fib(n - 1) + calc_fib(n - 2)


print("Welcome to the Recursive Artistry Program!")

# Menu loop
while True:
    print("Choose an option:\n1. Calculate Factorial")
    print("2. Find Fibonacci")
    print("3. Exit")

    c = input()

    if not validate_choice(c):
        continue

    match int(c):
        case 1:
            n = input("Enter a number to find its factorial: ")

            if validate_input(n):
                print(f"The factorial of {n} is {calc_fact(int(n))}.\n")
        case 2:
            n = input("Enter the position of the Fibonacci number: ")

            if validate_input(n):
                print(f"The Fibonacci number of position {n} is {calc_fib(int(n))}.\n")
        case _:
            exit(0)
