menu = {"pizza": 1000,
        "hotshots": 650,
        "freaky fries": 900,
        "twister rolls":1000,
        "pizza fries": 450,
        "cold drink" :350}
cart = []
total = 0
print("<-----MENU----->")
for key, value in menu.items():
    print(f"{key:15}: Rs{value:.2f}")
print("----------------")
print()
while True:
    food = input("Enter the food to buy(q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print("Selected item is not available")
print()
print("-----YOUR ORDER-----")        
for food in cart:
    total += menu.get(food)
    print(f"{food}: Rs{value}")
print(f"Your total is: Rs{total:.2f}")
print("--------------------")
