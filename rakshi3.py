contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }

    print("Contact added successfully!\n")


def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return

    print("\nContact List:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}")
    print()


def search_contact():
    query = input("Enter name or phone to search: ")

    found = False
    for name, details in contacts.items():
        if query == name or query == details["phone"]:
            print("\nContact Found:")
            print("Name:", name)
            print("Phone:", details["phone"])
            print("Email:", details["email"])
            print("Address:", details["address"])
            found = True
            break

    if not found:
        print("Contact not found.\n")


def update_contact():
    name = input("Enter name to update: ")

    if name in contacts:
        print("Enter new details (leave blank to keep old value):")

        phone = input("New phone: ")
        email = input("New email: ")
        address = input("New address: ")

        if phone:
            contacts[name]["phone"] = phone
        if email:
            contacts[name]["email"] = email
        if address:
            contacts[name]["address"] = address

        print("Contact updated successfully!\n")
    else:
        print("Contact not found.\n")


def delete_contact():
    name = input("Enter name to delete: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!\n")
    else:
        print("Contact not found.\n")


def menu():
    while True:
        print("===== CONTACT MANAGER =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice!\n")


menu()
