#a 2 dimensional list
#A list made up of list

"""fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meat = ["chicken", "fish", "turkey"]
"""
#list made of list
# groceries = [fruits, vegetables, meat]

#selecting in rows and column format
#print(groceries[2][1])

""" for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()
"""

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

# print the keypad without the brackets
for row in num_pad:
    for char in row:
        print(char, end=" ")
    print()

    