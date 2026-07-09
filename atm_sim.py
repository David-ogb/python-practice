balance = 0
# deposting function
def Deposit(val):
     deposit = int(input("Enter your deposit: "))
     val += deposit
     print(f"You have sucessfully deposited {deposit:.2f}")
     return val
     
    
# to withdraw
def Withdraw(val):    
    withdraw = int(input("How much do you want to withdraw: "))
    val -= withdraw
    return val
    # print(f"Your balance is {balance}")

# function to display the menu
def menu(balance):
    
    user_input = int(input("1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit\nEnter an option to begin: "))
    # to exit the program
    if user_input == 4:
        print('Thankyou for banking with us')
        return
    elif user_input == 1:
            balance = Deposit(balance)
            print(f"Your balance is {balance:.2f}")
    elif user_input == 2:
        balance = Withdraw(balance)
        print(f"Your balance is {balance:.2f}")
    elif user_input == 3:
        print(f"Your balance is {balance}")
    return balance

balance = menu(balance)
menu(balance)
balance = menu(balance)
# check if it's saved to balance
print(balance)