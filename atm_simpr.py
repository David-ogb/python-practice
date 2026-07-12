balance = 0
events = []
num_deposits = 0
num_withdrawals = 0

# deposting function
def Deposit(balance,num_deposits):
    try:
        deposit = float(input("Enter your deposit: "))
        if deposit < 0:
            print("You cannot enter a negative deposit")
        else:
            balance += deposit
            num_deposits += 1
            events.append(f"Deposit: +${deposit:.2f}")
            print(f"You have sucessfully deposited ${deposit:.2f}")
            return balance,num_deposits
    except ValueError:
        print("Enter an amount: ")    
        
# to withdraw
def Withdraw(balance,num_withdrawals):    
    try:
        withdraw = float(input("How much do you want to withdraw: "))
        if withdraw > balance:
            print("You cannot withdraw more than you have")
            return balance,num_withdrawals
        else:
            balance -= withdraw
            events.append(f"Withdraw: -${withdraw:.2f}")
            num_withdrawals += 1
            return balance,num_withdrawals
    except ValueError:
        print("Enter a proper value")
        

def history(events):
    print("History")
    print("==================")
    if len(events)!= 0:
        for event in events:
            print(event)
    else:
        print("No transaxtions yet")
    print("==================")

def summary(balance,num_deposits,num_withdrawals):
    print("====== SESSION SUMMARY =======")

    print(f"Final Balance: ${balance}")
    print(f"\nDeposits: {num_deposits}")
    print(f"Withdrawals: {num_withdrawals}\n")
    print("Thankyou for banking with us!")


# function to display the menu
def menu(balance,num_deposits, num_withdrawals):
    # to stop the infinite loop
    is_running = True
    while is_running:
        try:
            print("================================")
            print("BANKING PROGRAM")
            print("================================")
            user_input = int(input("1. Deposit\n2. Withdraw\n3. Check Balance\n4. History\n5. Exit\nEnter an option to begin: "))
            # to exit the program
            if user_input == 1:
                balance, num_deposits = Deposit(balance,num_deposits)
                print(f"Your balance is ${balance:.2f}")
            elif user_input == 2:
                balance, num_withdrawals = Withdraw(balance,num_withdrawals)
                print(f"Your balance is ${balance:.2f}")
            elif user_input == 3:
                print(f"Your balance is ${balance}")
            elif user_input == 4:
                history(events)
            elif user_input == 5:
                summary(balance,num_deposits,num_withdrawals)
                is_running = False
            else:
                print("Enter within the range of 1 - 4")
        except ValueError:
            print("Enter a suitable option")


menu(balance,num_deposits,num_withdrawals)