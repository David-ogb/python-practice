# A phone book mechanism
# Initializing an empty list to hold the names and numbers
names = []
phones = []

def add_contacts(names, phones):
    # the program runs infinitely
    while True:
        # enter your name before checking if u want to quit
        name = input("Enter a name (q to quit): ")   
        if name.lower() != "q":
            # updating the empty list
            names.append(name)     
            phone = int(input("Enter a number: "))
            phones.append(phone)
        else:
            return names, phones

# display the names and phone
def view_contacts(names, phones):
    # use the number of contacts/names to loop
    for x in range(len(names)):
        print(f"{names[x]}: {phones[x]}")
    menu()

def search_contact(names, phones):
    name = input("Enter a name: ")
    # name checks name(which is now a list because of the argument in menu)
    if name in names:
        # the position/index in the list
        y = names.index(name)
        print(f"{name} : {phones[y]}")
    else:
        print("Contact not found!")

def delete_contact(names, phones):
    delname = input("Enter a name: ")
    if delname in names:
        z = names.index(delname)
        names.remove(delname)
        phones.remove(phones[z])
        print(f"Deleted!")
        view_contacts(names, phones)
    else:
        print("Contact not found!")


def menu():
    while True:
        print()
        print("==== CONTACT BOOK ====\n")
        print("1. Add Contact\n2. View Contact\n3. Search Contact\n4. Delete Contact\n5. Exit")
        choice = int(input("Choose an option: "))
        if choice == 1:
            add_contacts(names, phones)
        elif choice == 2:
            view_contacts(names, phones)
        elif choice == 3:
            search_contact(names, phones)
        elif choice == 4:
            delete_contact(names, phones)
        elif choice == 5:
            return
        else:
            print("Enter something appropriate to start")
        

print(menu())
