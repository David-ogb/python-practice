import math

# ==========================================
# CALCULATOR PROJECT - Simple Version
# ==========================================

# Settings the user can change
config = {
    "decimal_places": 2
}

# Remembers the last result so it can be reused
state = {
    "previous_result": None
}

QUIT_WORDS = ["quit", "q", "exit", "e"]


# ----------- DISPLAY MESSAGES -----------

def info(message):
    print(f"ℹ️ {message}")

def success(message):
    print(f"✅ {message}")

def warning(message):
    print(f"⚠️ {message}")

def error(message):
    print(f"🚫 {message}")


# ----------- GETTING INPUT -----------

def get_number(prompt):
    # Ask for a number. Returns None if user quits.
    while True:
        info("Enter (quit/q/exit/e) to cancel current operation")
        user_input = input(prompt)

        if user_input.lower() in QUIT_WORDS:
            warning("Operation cancelled.")
            return None

        try:
            return float(user_input) #Convert text to a decimal number
        except ValueError:
            error("That is not a valid number")


def get_menu_choice(prompt, min_value, max_value):
    """Ask for a menu number between min_value and max_value."""
    while True:
        info("Enter (quit/q/exit/e) to cancel current operation")
        choice = input(prompt)

        if choice.lower() in QUIT_WORDS:
            return None

        try:
            choice = int(choice)#convert the choice from any to int
            if min_value <= choice <= max_value: #ensure it btw min and max
                return choice
            error("Invalid menu selection")
        except ValueError:
            error("Please enter a valid number")


# ----------- MATH OPERATIONS -----------

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b

def floor_div(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a // b

def mod(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a % b

def exp(num):
    return math.exp(num)

def power(base, exponent):
    return base ** exponent

def logarithm(number, base):
    if base <= 0 or base == 1:
        raise ValueError("Log base must be greater than 0 and not equal to 1")
    if number <= 0:
        raise ValueError("Log number must be greater than 0")
    return math.log(number, base)


# ----------- SHOWING A RESULT -----------

def show_result(value1, value2, result, label1="num1", label2="num2"):
    dp = config["decimal_places"]
    print("\n===== RESULT =====")
    if value1 is not None:
        print(f"{label1} = {value1:.{dp}f}")
    if value2 is not None:
        print(f"{label2} = {value2:.{dp}f}")
    print(f"Result = {result:.{dp}f}")

    success("Calculation completed")


# ----------- SETTINGS MENU -----------

def settings_menu():
    while True:
        print("\n===== ⚙️ SETTINGS =====")
        print("1. View Settings")
        print("2. Edit Settings")
        print("3. Return")

        choice = get_menu_choice("Choose option: ", 1, 3)

        if choice is None or choice == 3:
            return

        if choice == 1:
            print(f"\nDecimal Places = {config['decimal_places']}")

        elif choice == 2:
            new_value = get_number("Enter decimal places (0-9): ")

            if new_value is None:
                continue

            new_value = int(new_value)

            if 0 <= new_value <= 9:
                config["decimal_places"] = new_value
                success("Setting updated")
                print(f"New Value = {new_value}")
            else:
                error("Value must be between 0 and 9")


# ----------- GETTING THE TWO NUMBERS (with reuse) -----------

def get_two_numbers(label1="num1", label2="num2"):
    """
    Asks for two values, using whatever names you give it
    (e.g. "number"/"base" for Logarithm instead of "num1"/"num2").
    If a previous result exists, offers to reuse it as either value.
    Returns (value1, value2) or (None, None) if user quits.
    """
    previous = state["previous_result"]

    if previous is not None:
        answer = input(f"Reuse previous result ({previous})? (y/n): ")

        if answer.lower() == "y":
            position = input(f"Use previous result as {label1} or {label2}? ")

            if position.lower() == label1:
                value1 = previous
                value2 = get_number(f"Enter {label2}: ")
            else:
                value2 = previous
                value1 = get_number(f"Enter {label1}: ")

            return value1, value2

    # No reuse - ask for both values normally
    value1 = get_number(f"Enter {label1}: ")
    if value1 is None:
        return None, None

    value2 = get_number(f"Enter {label2}: ")
    return value1, value2


# ----------- CALCULATOR MENU -----------

def calculator_menu():
    while True:
        print("\n===== 📠 ARITHMETIC MENU =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Floor Division")
        print("6. Modulus")
        print("7. Exponential")
        print("8. Power")
        print("9. Logarithm")
        print("10. Return")

        choice = get_menu_choice("Choose operation: ", 1, 10)

        if choice is None or choice == 10:
            return

        try:
            # Exponential only needs ONE number
            if choice == 7:
                num = get_number("Enter number: ")
                if num is None:
                    continue
                result = exp(num)
                show_result(num, None, result)

            # All other operations need TWO numbers
            else:
                # Logarithm uses "number" and "base" instead of "num1"/"num2"
                # so it's clear that logarithm(number, base) = log_base(number)
                if choice == 9:
                    label1, label2 = "number", "base"
                else:
                    label1, label2 = "num1", "num2"

                num1, num2 = get_two_numbers(label1, label2)
                if num1 is None or num2 is None:
                    continue

                if choice == 1:
                    result = add(num1, num2)
                elif choice == 2:
                    result = sub(num1, num2)
                elif choice == 3:
                    result = mul(num1, num2)
                elif choice == 4:
                    result = div(num1, num2)
                elif choice == 5:
                    result = floor_div(num1, num2)
                elif choice == 6:
                    result = mod(num1, num2)
                elif choice == 8:
                    result = power(num1, num2)
                elif choice == 9:
                    result = logarithm(num1, num2)

                show_result(num1, num2, result, label1, label2)

            # Save this result so it can be reused next time
            state["previous_result"] = result

        except ZeroDivisionError:
            error("Zero division error encountered")
        except ValueError as e:
            error(str(e))


# ----------- MAIN MENU -----------

def main():
    while True:
        print("\n===== 📅 CALCULATOR MENU =====")
        print("1. Calculator")
        print("2. Settings")
        print("3. Exit")

        choice = get_menu_choice("Choose a menu: ", 1, 3)

        if choice is None:
            continue

        if choice == 1:
            calculator_menu()
        elif choice == 2:
            settings_menu()
        elif choice == 3:
            success("Thank you for using Calculator")
            break


main()