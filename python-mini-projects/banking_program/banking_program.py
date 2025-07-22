def balance(amount):
    print(f"Your Balance is:Rs.{amount:.2f}")

def deposit ():
    deposited_money = float(input("Enter the money to be deposited:Rs. "))  
    if deposited_money < 0:
        print("That is not a valid amount")
        return 0
    else:
        print(f"An amount of Rs.{deposited_money:.2f} was successfully deposited!🥳")
        return deposited_money
    
def withdrawal (balance):
    withdraw = float(input("Enter the amount to be withdrawn:Rs. "))
    if withdraw > balance:
        print("Insufficient funds! 😞")
        return 0 
    elif withdraw < 0:
        print("Amount MUST be greater than 0!")
        return 0
    else:
        print(f"An amount of Rs.{withdraw} was successfully withdrawn! ")
        return withdraw


def main():
    total_balance = 0
    is_running = True 

    while is_running:
        print("****** BANKING PROGRAM ******")
        print("What would you like to do:")
        print("1.Check Balance")
        print("2.Deposit Money")
        print("3.Withdraw Money")
        print("4.Exit")
        print("*****************************")
        print()
        choice = input("Select (1-4): ")
        if choice == "1":
            balance(total_balance)
        elif choice == "2":
            total_balance += deposit()
        elif choice == "3":
            total_balance -= withdrawal(total_balance)
        elif choice == "4":
            is_running = False
        else:
            print("Invalid Choice!")
            break
    print(f"Your balance is: Rs.{total_balance}")
    print("Thank you! Have a nice day")
if __name__ == '__main__':
    main()