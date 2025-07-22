foods = []
prices = []
total = 0

while True:
    food = input("Enter the food to buy(q to quit): ")
    if food.lower() == "q":
        break
    else:
        foods.append(food)
        price = float(input(f"What is the price of {food}:Rs "))
        prices.append(price)

print("-----YOUR CART-----")

for food in foods:
    print(food , end = " ")
print()

for price in prices:
    print(price, end = " ")

print()
for price in prices:
    total += price
print(f"Your total is: Rs{total}")