foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ").title()
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a{food}: $"))
        foods.append(food)
        prices.append(price)

print("----- Your Cart -----")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print(f"\nYour total is: ${total:.2f}")