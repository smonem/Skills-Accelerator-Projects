# Loops in Python

# Task 1
n = int(input("Enter the starting number: "))

while n > 0:
    print(n, end=" ")
    n -= 1

print("Blast off! 🚀")

# Task 2
n = int(input("\nEnter a number: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")


# Task 3
n = int(input("\nEnter a number: "))

factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"The factorial of {n} is {factorial}.")
