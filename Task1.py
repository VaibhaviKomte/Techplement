import json

def load_contacts():
    try:
        with open('contacts.json', 'r') as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []
    return contacts

def save_contacts(contacts):
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file, indent=2)

def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    # Validating that if contact name is not empty
    if not name:
        print("Error: Contact name cannot be empty.")
        return

    # Validating that if phone number is numeric
    if not phone.isdigit():
        print("Error: Invalid phone number. Please enter a numeric value.")
        return

    # Validating if  the email address is in a basic format
    if not '@' in email or not '.' in email:
        print("Error: Invalid email address format.")
        return

    contact = {'name': name, 'phone': phone, 'email': email}
    contacts.append(contact)
    print("Contact added successfully.")

def search_contact(contacts):
    name = input("Enter contact name to search: ")
    found_contacts = [contact for contact in contacts if contact['name'].lower() == name.lower()]

    if found_contacts:
        print(f"Contact details for '{name}':")
        for contact in found_contacts:
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
    else:
        print(f"Contact '{name}' not found.")

def update_contact(contacts):
    name = input("Enter contact name to update: ")
    found_contacts = [contact for contact in contacts if contact['name'].lower() == name.lower()]

    if found_contacts:
        print(f"Updating contact: {name}")
        new_phone = input("Enter new phone number: ")
        new_email = input("Enter new email address: ")

        # Validating if new phone number is numeric
        if not new_phone.isdigit():
            print("Error: Invalid phone number. Please enter a numeric value.")
            return

        # To validate if new email address is in a basic format
        if not '@' in new_email or not '.' in new_email:
            print("Error: Invalid email address format.")
            return

        for contact in found_contacts:
            contact['phone'] = new_phone
            contact['email'] = new_email
        print("Contact updated successfully.")
    else:
        print(f"Contact '{name}' not found.")

def main():
    contacts = load_contacts()

    while True:
        print("\nContact Management System:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            search_contact(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            save_contacts(contacts)
            print("Exiting. Contacts saved.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
