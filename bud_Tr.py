#program to track user budget
print("This is a program to gauge your financial health")
Income = 0
Expenses = []
#run infinitely 
print("Income|Expenses")
print("---------------")
print("00.00 |  00.00 ")
print("00.00 |  00.00 ")
print()
#giving the user options to take
print("press 1 to enter income,\n2 to enter expenses and \n3 to exit program")
#action taken by the user
act = int(input("What action would you like to take (1,2 or 3): "))

#run infinitely 
while True:
    #conditons within the range of the options provided
    if (act == 1) or (act == 2 ) or (act == 3):
        if act == 1:
            Income = float(input("Input your income for this month(3 to quit): "))
            
        elif act == 2:
            expense = float(input("Enter your expense: "))

        elif act == 3:
            break
    #ensure user satys on track
    else:
        print("You can only pick from the options")
        act = int(input("What action would you like to take (1,2 or 3): "))
