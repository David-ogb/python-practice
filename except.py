# Exceptions = An event that interupts the program flow
        # (ZeroDivisionError, TypeError, ValueError)
#          try, 2. except, 3. finally


"""try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Enter only numbers")"""


try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Enter only numbers")
except Exception:
    print("Something went wrong!")
finally:
    print("Do some clean up")