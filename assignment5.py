# Functions in Python

# Task 1


def greet_user(name):
    print(f"Hello, {name}! Welcome aboard.")


def add_numbers(n1, n2):
    return n1 + n2


# Example output
greet_user("Alice")
print(f"The sum of 5 and 10 is {add_numbers(5, 10)}.")

# Task 2


def describe_pet(pet_name, animal_type="dog"):
    print(f"\nI have a {animal_type} named {pet_name}.")


# Example output
describe_pet("Buddy")
describe_pet("Whiskers", "cat")

# Task 3


def make_sandwich(*ingredients):
    print("\nMaking a sandwich with the following ingredients:", end="")
    for ingredient in ingredients:
        print(f" - {ingredient}", end="")
    print()


# Example output
make_sandwich("Lettuce", "Tomato", "Cheese")

# Task 4


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Example output
print(
    f"\nFactorial of 5 is {factorial(5)}. The 6th Fibonacci number is {fibonacci(6)}."
)
