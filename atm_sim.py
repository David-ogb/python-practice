# deposting function
def Deposit(balance):
     deposit = int(input("Enter your deposit: "))
     balance += deposit
     print(f"You have sucessfully deposited {deposit:.2f}")
     return balance
     
    
# to withdraw
def Withdraw(balance):    
    withdraw = int(input("How much do you want to withdraw: "))
    balance -= withdraw
    return balance
    # print(f"Your balance is {balance}")

# function to display the menu
def menu(balance):
    is_running = True
    while is_running:
        user_input = int(input("1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit\nEnter an option to begin: "))
        # to exit the program
        if user_input == 4:
            print('Thankyou for banking with us')
            is_running = False
        elif user_input == 1:
                balance = Deposit(balance)
                print(f"Your balance is {balance:.2f}")
        elif user_input == 2:
            balance = Withdraw(balance)
            print(f"Your balance is {balance:.2f}")
        elif user_input == 3:
            print(f"Your balance is {balance}")

balance = 0
menu(balance)