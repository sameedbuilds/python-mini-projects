weight = float(input("What is your weight?: "))
unit = input("Kiloagrams or pounds?(K or L): ")

if unit == "K":
    weight *= 2.205
    unit = "Lbs."
    print(f"You weigh: {round(weight,1)} {unit}")
elif unit == "L":
    weight /= 2.205
    unit = "Kgs."
    print(f"You weigh: {round(weight,1)} {unit}")
else:
    print(f"{unit} as a unit was not valid!")