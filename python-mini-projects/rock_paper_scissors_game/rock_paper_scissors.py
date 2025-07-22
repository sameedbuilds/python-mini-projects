import random
game_choice = ("rock", "paper","scissors")

player_score = 0
computer_score = 0
is_running = True
while is_running:
    player = None
    computer = random.choice(game_choice)
    player = input("Enter a choice(rock,paper,scissors):")
    if player not in game_choice:
        print("Invalid choice made")
    else:
        print(f"Your choose: {player}")
        print(f"Computer choose: {computer}")
    if player == computer:
        print("It is a tie!!")
    elif player == "rock" and computer == "scissors":
        print("You Win!🥳")
        player_score +=1
    elif player == "scissors" and computer == "paper":
        print("You Win!🥳")
        player_score +=1
    elif player == "paper" and computer == "rock": 
        print("You Win!🥳")
        player_score +=1
    else:
        print("You Lose😓")
        computer_score +=1
    print()
    if input("Do u want to continue:(Yes/No)").lower() not in ("yes" or "y"):
        is_running = False
print(f"Your score is: {player_score}")
print(f"Computer's score is: {computer_score}")
print("Thanks for playing, BYE!")