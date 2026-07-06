#concession stand program

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "Ice cream": 2.50,
        "fries": 1.50,
        "soda": 3.00}

cart = []
total = 0
print("---------MENU----------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("-"*25)

while True:
    food = input("select an item(q to quit): ")
    if food.lower() == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

#total
for food in cart:
    total += menu.get(food)
print(f"Total is ${total:.2f}")