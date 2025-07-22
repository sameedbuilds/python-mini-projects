import random
low_num = 1
high_num = 100
guesses = 0
is_running = True
number = random.randint(low_num, high_num)
print("--WELCOME TO THE PYTHON WORD GUESSING GAME!!")
print(f"Enter a number between {low_num} and {high_num} to start")
while is_running:
    guess =input("Enter your number:")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("INVALID❗")
            print("The number u entered is out of range 😞")
        elif guess > number:
            print("INCORRECT❌ TOO HIGH!")
        elif guess < number:
            print("INCORRECT❌ TOO LOW!")
        else:
            print("CORRECT✅")
            print(f"It took you {guesses} guesses to win!")
    else:
        print("INVALID❗")
        print("Please enter a valid number to play")
    

