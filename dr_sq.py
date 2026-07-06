#draw a square
"""nums = int(input("Enter a number: "))

for row in range(nums):
    for col in range(nums):
        print("*", end="")
    print()"""

#Multiplication table

"""number = int(input("Enter a number for a multiplication table: "))

count = 0
for x in range(13):
    print(f"{number} * {count} = {number * count}")
    count += 1
print("End")"""

#Multiplication table 12x12 grid

"""for x in range(1, 13):
    for y in range(1, 13):
        print(y * x,end=" ")
    print()"""

def square(num):
    return num ** 2

def calc_area(length, width):
    area = length * width
    return area

def is_even(num):
    return num % 2 == 0


print(is_even(8))
