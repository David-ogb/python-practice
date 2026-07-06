#A program to check a password strenght


password = input("password: ")

has_letter = False
has_number = False

for char in password:
    if char.isalpha():
        has_letter = True
    if char.isdigit():
        has_number = True

if len(password) >= 8 and has_letter and has_number:
    print("Strong password")
else:
    print("Weak password")

