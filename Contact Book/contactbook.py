# ============================================
# Contact Book App - Menu-driven contact manager
# Stores contacts in a dictionary of dictionaries:
# contacts[name] = {'age':.., 'email':.., 'mobile':..}
# ============================================

# Dictionary to hold all contacts, empty at start
contacts = {}

# Keep showing the menu until user chooses to exit
while True:
    print('\nContact Book App')
    print('1. Create contact')
    print('2. View contact')
    print('3. Update contact')
    print('4. Delete contact')
    print('5. Search contact')
    print('6. Count contact')
    print('7. Exit')

    choice = input('Enter your choice=')

    # --- Create a new contact ---
    if choice == '1':
        name = input("Enter your name=")
        if name in contacts:
            # Avoid overwriting an existing contact
            print(f"Contact name {name} already exists!")
        else:
            age = input("Enter age=")
            email = input("Enter email=")
            mobile = input("Enter mobile number=")
            # Store this contact's details as a nested dictionary
            contacts[name] = {
                'age': int(age),
                'email': email,
                'mobile': mobile
            }
            print(f"Contact name {name}has been created successfully")

    # --- View an existing contact ---
    elif choice == '2':
        name = input("Enter contact name to view:")
        if name in contacts:
            contact = contacts[name]
            # This prints the loop's leftover age/mobile variables
            # instead of contact['age']/contact['mobile'], so it only
            # looks correct if those were set earlier by chance
            print(f'Name: {name}, Age: {age}, Mobile Number:{mobile}')
        else:
            print('COntact not found')

    # --- Update an existing contact ---
    elif choice == '3':
        name = input("Enter name to update contact=")
        if name in contacts:
            age = input("Enter updated age=")
            email = input("Enter updated email=")
            mobile = input("Enter updated mobile number= ")
            # Overwrite the old record with the new details
            contacts[name] = {
                'age': int(age),
                'email': email,
                'mobile': mobile
            }
        else:
            print('Contact not found')

    # --- Delete a contact ---
    elif choice == '4':
        name = input("Enter contact name to delete=")
        if name in contacts:
            del contacts[name]
            print(f"Contact name {name} has been deleted successfully!")
        else:
            print('Contact not found')

    # --- Search contacts by partial, case-insensitive name match ---
    elif choice == '5':
        search_name = input("Enter contact name to search=")
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                # Some issue as "View contact" - should read from
                # contact['age'], contact['mobile'], contact['email']
                print(f"Found -Name {name}, Age:{age}, Mobile Number: {mobile}, Email:{email}")
                found = True
            # This check runs inside the loop, so "No contact found"
            # can print once per non-matching contact instead of just once
            # after checking everyone
            if not found:
                print('No contact found with that name')

    # --- Show total number of saved contacts ---
    elif choice == '6':
        print(f"Total contacts in your book:{len(contacts)}")

    # --- Exit the program ---
    elif choice == '7':
        print("Good bye..Closing the program")
        break

    else:
        print("Invalid Input")