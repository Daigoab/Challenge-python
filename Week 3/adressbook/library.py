
def parse_file(file_path):
    address_book = {}
    with open(file_path, "r") as file:
        for line in file:
            name, address = line.strip().split(", ")
            address_book[name] = address
    return address_book

def add_entry(file_path, name, address):
    with open(file_path, "a") as file:
        file.write(f"\n{name}, {address}")

file_path = "C:/Users/HP/Desktop/code/adressbook"

# Example usage:
address_book = parse_file(file_path)
print(address_book)

new_name = input("Enter a name: ")
new_address = input("Enter an address: ")
add_entry(file_path, new_name, new_address)
print(f"Added {new_name} to the address book.")

# Print updated address book
address_book = parse_file(file_path)
print(address_book)

