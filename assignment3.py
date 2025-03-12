# Strings in Python

# Task 1
s = "Python is amazing!"

fword = s[:6]
aword = s[10:18]
rs = s[::-1]

print(f"First word: {fword}")
print(f"Amazing part: {aword}")
print(f"Reversed string: {rs}")


# Task 2
s = " hello, python world! "

print(f"\nStripped: '{s.strip()}'")
print(f"Capitalized: '{s.strip().capitalize()}'")
print(f"Replaced: '{s.replace("world", "universe")}'")
print(f"Uppercase: '{s.upper()}'")


# Task 3
w = input("\nEnter a word: ")

if w == w[::-1]:
    print(f"Yes, '{w}' is a palindrome!")
else:
    print(f"No, '{w}' is not a palindrome.")
