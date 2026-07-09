balance = 0

# to redo the programme
def get_choice():
    user_input = int(input("1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit\nEnter an option to begin: "))
    # to exit the program
    while user_input <= 4:
        try:
            if user_input == 4:
                print('Thankyou for banking with us')
                break
            elif user_input == 1:
                Deposit()
            elif user_input == 2:
                Withdraw()
            elif user_input == 3:
                print(f"Your balance is {balance}")
                get_choice()
        except ValueError:
            print("Please enter within the range of 1 - 3")
            return

# deposting function
def Deposit():
     balance = 0 
     deposit = int(input("Enter your deposit: "))
     balance += deposit
     print(f"Your balance is {balance:.2f}")
     get_choice()

# to withdraw
def Withdraw():
    balance = 0 
    withdraw = int(input("How much do you want to withdraw: "))
    balance -= withdraw
    print(f"Your balance is {balance}")
    get_choice()

# function to display the menu
def menu():
    balance = 0
    user_input = int(input("1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit\nEnter an option to begin: "))
    # to exit the program
    while user_input <= 4:
        try:
            if user_input == 4:
                print('Thankyou for banking with us')
                break
            elif user_input == 1:
                Deposit()
            elif user_input == 2:
                Withdraw()
            elif user_input == 3:
                print(f"Your balance is {balance}")
                get_choice()
        except ValueError:
            print("Please enter within the range of 1 - 3")
            return

menu()