temp = float(input("What is the temperature?: "))
unit = input("Is it in Celsius or Farenheit (C/F)?: ")
if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature is {temp}°F")
elif unit == "F":
    temp = round((temp-32) * 5/9, 1)
    print(f"The temperature is {temp}°C")
else:
    print (f"{unit} is an invalid unit of measurement :(")