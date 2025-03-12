# Eligible Elector

age = input("How old are you? ")

# Error Checking
if not str.isnumeric(age) or int(age) < 1:
    print("Error: invalid input.")
    exit(0)

age = int(age)
if age < 18:
    print(
        f"Oops! You’re not eligible yet. But hey, only {18 - age} more year{"s" if age != 17 else ""} to go!"
    )
else:
    print("Congratulations! You are eligible to vote. Go make a difference!")
