principle_amount = 0
interest_rate = 0
time = 0

while True :
    principle_amount= float(input("Enter your initial investment: "))
    if principle_amount < 0:
        print("Investment cant be less than 0 to proceed!")
    else:
        break
while True:
    interest_rate = float(input("Enter the interest rate: "))
    if interest_rate < 0:
        print("Interest rate cant be less than 0 to proceed!")
    else:
        break
while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time passed cant be less than 0 to proceed!")
    else:
        break

Total_capital = principle_amount * pow((1 + interest_rate/100), time )
print(f"Your total capital after {time} year/s is Rs{Total_capital:.2f}")