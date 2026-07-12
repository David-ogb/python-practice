#functions
import time

"""def count(end, start = 0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Time Up")

count(30, 15)"""

# Kwargs
"""def hello(last, greeting, title, first):
    print(f"{greeting} {title} {first} {last}")

hello("Squarepants", title="Mr", greeting="Hello", first="spongebob")"""

# for x in range(1, 11):
    # print(x, end="")

"""def get_phone(country, area, first, last):
    return f"{country}--{area}--{first}--{last}"

phone_num = get_phone(country=1, area=123, first=984, last=564)
print(phone_num)"""

#to add avarying amount of arguments
"""def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total


print(add(1, 2, 3))"""

"""def name(*names):
    for name in names:
        print(f"{name}")
    return name

name("James","Samuel","Johnny")"""

# **Kwargs
"""def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Fake St.", city="Manchester", state="London")"""

#Shipping label

"""def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')}")

shipping_label("Dr.", "Spongebob", "squre", "The third", street="123 Fake",
               city="Detroit",
               state="Florida")"""


#Iterables = any obj/collection that can return its element one at a time
"""name = {"A": 1, "B": 2, "C":3}

for key, value in name.items():
    print(key, value)"""

#Memebership in and not in

"""word = "APPLE"

letter = input("guess a letter in the word: ")
if letter.lower() in word.lower():
    print(f"There is a {letter} in the word")"""

"""grades = {"sandy": "A",
          "patrick": "E",
          "spongebob": "A",
        "squidward": "B"}

student = input("Enter the name of the student: ")

if student in grades:
    print(f"{student} got a {grades.get(student)}!") 
else:
    print(f"{student} is not found")"""

"""email = "brocd@gmailcom"

if "@" in email and "." in email:
    print("VAlide email")
else:
    print("Invalid email")"""

#list comprehension - better way to list in python

# doubles = []

# for x in range(1, 11):
    # doubles.append(x * 2)
# print(doubles)

# double = [expression for value in iterable if condition ]

"""doubles = [x * 2 for x in range(1,11)]
triples = [y ** 3 for y in range(1, 11)]

print(triples)"""

# fruits = ["apples", "orange", "banana", "coconut"]
# fruits = [fruit.capitalize() for fruit in fruits]

# print(fruits)

# Modulers - a file with code you want to include in your program
#              using import 


# import exmod as egg

# result = egg.pow(3, 4)
# print(result)

# variable scope - both visible and accessible
# scope resolution - LEGB Local -> Enclosed --> Global -->Built-in

# var in function is local

# def main():
#     # Yiur origran goes here


# if __name__ == '__main__':
#     main()


# Banking program
"""
def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to be deposited: "))

    if amount < 0:
        print("That's not a valid amount")
        return 0
    else:
        return amount
def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn: "))

    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print ("amount must be greater than 0")
        return 0
    else:
        return amount
    
def main():
    balance = 0
    is_running = True

    while is_running:

        print("************************\n")
        print("BANKING PROGRAM\n")
        print("************************")
        choice = int(input("1. show balance\n2. Deposit\n3. Withdraw\n4. Exit\n************************\nEnter an option to begin: "))
        

        if choice == 1:
            show_balance(balance)
        elif choice == 2:
            balance += deposit()
        elif choice == 3:
            balance -= withdraw(balance)
        elif choice == 4:
            is_running = False
        else:
            print("Enter a valid option")

    print("Thankyou for banking with us!")

if __name__ == '__main__':
    main()
"""


# OOP
#  object = a "bundle" of related attribute (variables) and methods(functions)
            # E.g phone, cup, book
            # You need a 'Class' to create many objects

# class = blueprint to design an object

# from car import Car

# car1 = Car("Mustang",2025,"Black",True)
# car2 = Car("Corvette", 2021, "blue", False)

# car1.details()
# car2.details()
"""
class Student:

    class_year = 2025
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1
        
student1 = Student("David", 29)
student2 = Student("Amos", "31")
student3 = Student("James", 29)
student4 = Student("Jennifer", "26")

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name)  
print(student2.name)  
print(student3.name)  """


# Inheritance

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Mouse(Animal):
    pass

dog = Dog("Scobby")
cat = Cat("garfield")
mouse = Mouse("Mickey")

print(cat.is_alive)
cat.sleep()
cat.eat()


        