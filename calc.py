#Code to run as a calculator

#take in the first number
num1 = int(input("Enter the first number: "))

#take in the second number
num2 = int(input("Enter the first number: "))

operator = input("Enter an operator (/, +, -, *): ")

#division
if operator == "/":
    answer = num1 / num2
    print(f"{num1} / {num2} = {answer:.2f}")

#addition
elif operator == "+":
    answer = num1 + num2
    print(f"{num1} + {num2} = {answer:.2f}")

#subtraction
elif operator == "-":
    answer = num1 - num2
    print(f"{num1} - {num2} = {answer:.2f}")

#multiplication
elif operator == "*":
    answer = num1 * num2
    print(f"{num1} * {num2} = {answer:.2f}")