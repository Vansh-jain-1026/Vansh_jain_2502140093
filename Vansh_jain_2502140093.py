def authenticate_user():
    PASSWORD = "admin123"
    attempts = 3
    while attempts > 0:
        entered = input("Enter password to access the system: ")
        if entered == PASSWORD:
            print("Access granted!\n")
            return True
        else:
            attempts -= 1
            print(f"Incorrect password. {attempts} attempts left.\n")
    print("Access denied! Exiting program.")
    return False



inventory = {}
categories = set()
def add_item(inventory):
    item_id = input("Enter item ID: ").strip()
    if item_id in inventory:
        print("Item ID already exists! Try modifying it instead.\n")
        return

    name = input("Enter item name: ")
    stock = int(input("Enter stock count: "))
    price = float(input("Enter price per unit: "))
    category = input("Enter category: ")

    inventory[item_id] = {
        "name": name,
        "stock": stock,
        "price": price,
        "category": category,
        "description": ("Brand not specified", "Generic Product")  # Example tuple
    }
    categories.add(category)
    print(f"Item '{name}' added successfully!\n")


def modify_item(inventory):
    item_id = input("Enter the item ID to modify: ").strip()
    if item_id not in inventory:
        print("Item not found.\n")
        return

    print(f"Current details: {inventory[item_id]}")
    stock = int(input("Enter new stock count: "))
    price = float(input("Enter new price: "))
    inventory[item_id]["stock"] = stock
    inventory[item_id]["price"] = price
    print("Item updated successfully!\n")


def delete_item(inventory):
    item_id = input("Enter the item ID to delete: ").strip()
    if item_id in inventory:
        del inventory[item_id]
        print("Item deleted successfully!\n")
    else:
        print("Item not found!\n")


def search_item(inventory):
    query = input("Enter item name or ID to search: ").strip().lower()
    results = []
    for item_id, details in inventory.items():
        if query in item_id.lower() or query in details["name"].lower():
            results.append((item_id, details))
    if results:
        print("\nSearch Results:")
        for item_id, details in results:
            print(f"ID: {item_id}, Name: {details['name']}, Stock: {details['stock']}, Price: ₹{details['price']}")
    else:
        print("No matching items found.\n")


# Reporting Functions

def total_stock_value(inventory):
    total_value = sum(details["stock"] * details["price"] for details in inventory.values())
    print(f"Total stock value: ₹{total_value:.2f}\n")


def low_stock_items(inventory):
    print("Items with low stock (<5):")
    for item_id, details in inventory.items():
        if details["stock"] < 5:
            print(f"{item_id}: {details['name']} (Stock: {details['stock']})")
    print()


def category_summary(inventory):
    category_counts = {}
    for details in inventory.values():
        category = details["category"]
        category_counts[category] = category_counts.get(category, 0) + details["stock"]
    print("\nCategory-wise Stock Summary:")
    for cat, total in category_counts.items():
        print(f"{cat}: {total} items")
    print()


def view_reports(inventory):
    print("\n--- Reports Menu ---")
    print("1. Total Stock Value")
    print("2. Low Stock Items")
    print("3. Category Summary")
    choice = input("Enter your choice: ")
    if choice == "1":
        total_stock_value(inventory)
    elif choice == "2":
        low_stock_items(inventory)
    elif choice == "3":
        category_summary(inventory)
    else:
        print("Invalid option.\n")



def display_menu():
    print("\n--- Stationery Shop Inventory ---")
    print("1. Add Item")
    print("2. Modify Item")
    print("3. Delete Item")
    print("4. Search Item")
    print("5. View Reports")
    print("6. Exit")
    return input("Enter your choice: ")


def main():
    if not authenticate_user():
        return

    while True:
        choice = display_menu()

        if choice == "1":
            add_item(inventory)
        elif choice == "2":
            modify_item(inventory)
        elif choice == "3":
            delete_item(inventory)
        elif choice == "4":
            search_item(inventory)
        elif choice == "5":
            view_reports(inventory)
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()