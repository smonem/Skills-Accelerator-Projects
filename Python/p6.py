# Calculator with Exception Handling


# Test choice validity
def validate_choice(i):
    if not i.isnumeric() or int(i) not in range(1, 6):
        print("Invalid input")
        return False
    return True


# Get input and check validity
def get_nums():
    a = input("Enter the first number: ")
    if not a.isnumeric():
        raise ValueError("Invalid input! Please enter a valid number.")
    b = input("Enter the second number: ")
    if not a.isnumeric():
        raise ValueError("Invalid input! Please enter a valid number.")

    return a, b


print("Welcome to the Error-Free Calculator!")

# Menu loop
while True:
    print("Choose an operation:\n1. Addition")
    print("2. Subtraction ")
    print("3. Multiplication")
    print("4. Division ")
    print("5. Exit")

    c = input()

    if not validate_choice(c):
        continue

    match int(c):
        case 1:
            try:
                a, b = get_nums()
                print(int(a) + int(b))
            except ValueError as e:
                print(e)
        case 2:
            try:
                a, b = get_nums()
                print(int(a) - int(b))
            except ValueError as e:
                print(e)
        case 3:
            try:
                a, b = get_nums()
                print(int(a) * int(b))
            except ValueError as e:
                print(e)
        case 4:
            try:
                a, b = get_nums()
                print(int(a) / int(b))
            except ValueError as e:
                print(e)
            except ZeroDivisionError as e:
                print("Oops! Division by zero is not allowed.")
        case _:
            print("Goodbye!")
            exit(0)
