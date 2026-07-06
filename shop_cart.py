#shopping cart program

foods = []
prices = []
total = 0

while True:
#take in user input
    food = input("Enter a food you want(q to quit): ")
#for extra usability
    if food.lower() == "q":
        break
    else:
        price = float(input(f"How much does a {food} cost? $"))
        foods.append(food)
        prices.append(price)

print("------------YOUR CART ------------")
for food in foods:
    print(food, end =' ')

for price in prices:
    total += price

print()
print(f"Your total is {total}")



