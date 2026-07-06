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

fruits = ["apples", "orange", "banana", "coconut"]
fruits = [fruit.capitalize() for fruit in fruits]

print(fruits)