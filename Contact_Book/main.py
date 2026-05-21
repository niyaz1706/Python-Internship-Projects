contacts = []
while True:
    print("\n===== Contact Book =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        contact = {
            "name": name,
            "phone": phone
        }
        contacts.append(contact)
        print("✅ Contact Added Successfully")
    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts found")
        else:
            print("\nSaved Contacts:")
            for contact in contacts:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}")
    elif choice == "3":
        search_name = input("Enter name to search: ")
        found = False
        for contact in contacts:
            if contact["name"].lower() == search_name.lower():
                print(f"Found Contact: {contact}")
                found = True
        if not found:
            print("❌ Contact Not Found")
    elif choice == "4":
        delete_name = input("Enter name to delete: ")
        found = False
        for contact in contacts:
            if contact["name"].lower() == delete_name.lower():
                contacts.remove(contact)
                print("🗑️ Contact Deleted Successfully")
                found = True
        if not found:
            print("❌ Contact Not Found")
    elif choice == "5":
        print("Exiting Contact Book...")
        break
    else:
        print("❌ Invalid Choice. Please Try Again.")