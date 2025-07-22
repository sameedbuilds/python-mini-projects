import random
import time
def spin_rows():
    rows = ["🍒", "🍍", "🍋", "🔔" , "⭐"]
    return [(random.choice(rows)) for _ in range(3)]

def display_rows(row):
    print("***************")
    print(" | ".join(row) )
    print("***************")

def get_payout(bet , row):
    if row[0] == row[1] == row[2]:
         if row[0] == "🍒":
              return bet * 2
         elif row[0] == "🍋":
              return bet * 4
         elif row[0] == "🍍":
              return bet * 6
         elif row[0] == "🔔":
              return bet * 8
         elif row[0] == "⭐":
              return bet * 10
    else:
        return 0 

def main():
    is_running = True
    balance = 100
    while is_running:
        print("*****PYTHON SLOT MACHINE*****")
        print("Symbols: 🍒,🍍,🍋,🔔,⭐")
        
        print (f"Your starting balance is: Rs.{balance}")

        bet = input("Enter your bet to start: Rs.")

        if not bet.isdigit():
            print("Enter a valid bet to start!")
            continue

        bet = int(bet)
                     
        if bet > balance:
                print ("Insufficient funds!")
                choice1 = input("Do u want to play again?(Y/N):").upper()
                if choice1 != "Y":
                    break
        if bet <= 0 :
             print("Bet Is not Valid!")
             continue
        
        balance -= bet
        row = spin_rows()
        print("Spinning...\n")
        time.sleep(1)
        display_rows(row)
            
        payout = get_payout(bet , row)
        if payout > 0:
             print(f"You won!🥳")
             balance += payout
             print(f"Your balance is now :Rs.{balance}")
        else:
             print("You lost!😓")
             print(f"Your balance is:Rs.{balance}")

        choice2 = input("Do u want to play again?(Y/N):").upper()
        if choice2 != "Y":
             break
    print("Thanks for playing!")
    print(f"Your ending balance is:Rs.{balance}")

if __name__ == '__main__':
        main()

