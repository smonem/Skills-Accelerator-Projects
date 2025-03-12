# Implement Data Structures


# Test choice validity
def validate_choice(i):
    if not i.isnumeric() or int(i) not in range(1, 5):
        print("Invalid input")
        return False
    return True


# Print formatted inventory item
def print_item(k, i):
    print(f"Item: {k}, Quantity: {i[0]}, Price: ${i[1]}")


# Add or update item in inventory
def update_item(inv, name, p, q):
    # Validation
    if len(name) == 0 or not q.isdigit() or not p.replace(".", "", 1).isdigit():
        print("Invalid input\n")
        return False
    else:
        inv[name] = (int(q), float(p))
    return True


# Print entire inventory and total cost
def print_inv(inv):
    print("Updated inventory:")
    for k, v in inv.items():
        print_item(k, v)

    print(
        f"Total value of inventory: ${sum([p[0] * p[1] for p in inventory.values()]):.1f}\n"
    )


# Select existing item by name
def select_item(inv):
    if len(inv.values()) == 0:
        print("Inventory empty\n")
        return None

    item = input(f"\nSelect an item by name: ")

    if item not in inv.keys():
        print("Invalid input\n")
        return None

    return item


print("Welcome to the Inventory Manager!")

inventory = {}
inventory["apple"] = (10, 2.5)
inventory["banana"] = (20, 1.2)


# State of initial inventory
print("Current inventory:")
for k, v in inventory.items():
    print_item(k, v)
print()

# Menu loop
while True:
    print("1. Add new item")
    print("2. Remove item")
    print("3. Update item")
    print("4. Exit")

    c = input()

    if not validate_choice(c):
        continue

    match int(c):
        case 1:
            name = input("\nEnter name: ")
            q = input("Enter quantity: ")
            p = input("Enter price: ")

            if update_item(inventory, name, p, q):
                print(f"Adding a new item: {name}\n")
                print_inv(inventory)
        case 2:
            i = select_item(inventory)
            if i:
                del inventory[i]
                print(f"Removing item: {i}\n")
                print_inv(inventory)
        case 3:
            i = select_item(inventory)
            if i:
                q = input("Enter new quantity: ")
                p = input("Enter new price: ")
                if update_item(inventory, i, p, q):
                    print(f"Updating item: {i}\n")
                    print_inv(inventory)
        case _:
            exit(0)
