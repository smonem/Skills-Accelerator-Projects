# Number Guessing

import random

number_to_guess = random.randint(1, 100)
n_attempts = 0

# Main loop
while True:
    n = input("Guess the number (between 1 and 100): ")

    if not n.isnumeric() or int(n) < 1 or int(n) > 100:
        print("Invalid input")
        continue

    n_attempts += 1

    if n_attempts >= 10:
        print("Game over! Better luck next time!")
        exit(0)

    n = int(n)
    if n > number_to_guess:
        print("Too high! Try again.")
    elif n < number_to_guess:
        print("Too low! Try again.")
    else:
        print(
            f"Congratulations! You guessed it in {n_attempts} attempt{"s"[:n_attempts^1]}!"
        )
        exit(0)
