# Data Structures in Python

# Task 1

fruits = ["apple", "banana", "cherry", "date", "strawberry"]
print(f"Original list: {fruits}")

fruits.append("fig")
print(f"After adding a fruit: {fruits}")

fruits.remove("apple")
print(f"After removing a fruit: {fruits}")

reversed_fruits = fruits[::-1]
print(f"Reversed list: {reversed_fruits}")


# Task 2
info = {"name": "Saad", "age": 26, "city": "Ypsi"}

info["favorite color"] = "Black"
info["city"] = "Chicago"

print("\nKeys: ", [k for k in info.keys()])
print("Values: ", [v for v in info.values()])


# Task 3
favs = ("Avengers: Infinity War", "Barbie Girl", "Catch-22")
print(f"\nFavorite things: {favs}")

try:
    favs[0] = "Avengers: Endgame"
except TypeError:
    print("Oops! Tuples cannot be changed.")

print(f"Length of tuple: {len(favs)}")
