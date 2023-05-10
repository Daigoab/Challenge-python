import csv

class InventoryItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.quantity} x ${self.price}"

class InventoryManagement:
    def __init__(self):
        self.inventory = []

    def add_item(self, name, quantity, price):
        item = InventoryItem(name, quantity, price)
        self.inventory.append(item)

    def remove_item(self, name):
        self.inventory = [item for item in self.inventory if item.name != name]

    def update_item(self, name, quantity=None, price=None):
        for item in self.inventory:
            if item.name == name:
                if quantity is not None:
                    item.quantity = quantity
                if price is not None:
                    item.price = price

    def display_inventory(self):
        for item in self.inventory:
            print(item)

    def load_inventory(self, filename):
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                name, quantity, price = row
                self.add_item(name, int(quantity), float(price))

    def save_inventory(self, filename):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            for item in self.inventory:
                writer.writerow([item.name, item.quantity, item.price])

def main():
    inventory_manager = InventoryManagement()

    # Load initial inventory from file
    inventory_manager.load_inventory("inventory.csv")

    # User menu
    while True:
        print("\nInventory Management System\n")
        print("1. Add item")
        print("2. Remove item")
        print("3. Update item")
        print("4. Display inventory")
        print("5. Save inventory to file")
        print("6. Exit")
        choice = input("\nEnter choice: ")

        if choice == "1":
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            inventory_manager.add_item(name, quantity, price)
            print("Item added successfully")

        elif choice == "2":
            name = input("Enter item name: ")
            inventory_manager.remove_item(name)
            print("Item removed successfully")

        elif choice == "3":
            name = input("Enter item name: ")
            quantity = input("Enter new quantity (leave blank to keep current): ")
            price = input("Enter new price (leave blank to keep current): ")
            if quantity:
                quantity = int(quantity)
            if price:
                price = float(price)
            inventory_manager.update_item(name, quantity, price)
            print("Item updated successfully")

        elif choice == "4":
            inventory_manager.display_inventory()

        elif choice == "5":
            filename = input("Enter filename to save inventory to: ")
            inventory_manager.save_inventory(filename)
            print("Inventory saved to file")

        elif choice == "6":
            # Save inventory to file before exiting
            inventory_manager.save_inventory("inventory.csv")
            print("Exiting program")
            break

        else:
            print("Invalid choice, please try again")

if __name__ == "__main__":
    main()
