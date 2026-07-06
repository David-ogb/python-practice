#program for a fairly complex calculator
import math

state = {
    "previous_result": None,
    "reuse": False,
    "current_operation": None
}
config = {
    "decimal_places": 2
}

def info(msg):
    print(f"ℹ️ {msg}")

def success(msg):
    print(f"✅ {msg}")

def warning(msg):
    print(f"⚠️ {msg}")

def error(msg):
    print(f"🚫 {msg}")

#print the calculator menu
print("___Welcome to the command line calculator____")
print()
print("Click 1 to enter calculator")
print("Click 2 to enter Settings")
print("Click 3 to Exit the calculator programme")

#Set a container to help user navigate
initial = int(input("Enter an option to continue (press q/ e /quit/ exit to leave): "))
#the calculator menu
if initial == 1:
    print("Welcome to the calculator")
    #display calculator option   
    print("1. Add \n2. Sub \n3. Mul\n4. Div\n5. FloorDiv\n6. Mod\n7. Exp\n8. Pow\n9. Log")
    #choose an operator to perform
    operator = int(input("Enter an operator to begin (to exit q, e, quit, exit)"))


#settings menu
elif initial == 2:
    print("Welcome to the Settings")
#exiting
elif initial == 3:
    print("Thankyou Goodbye")

