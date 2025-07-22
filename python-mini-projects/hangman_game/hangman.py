import random
from wordslist import words
hangman_art = {0:("      ",
                 "       ",
                 "       "),
               1:("  o   ",
                  "      ",
                  "      "),
               2 :(" o   ",
                   " |   ",
                   "     "),
               3 :(" o   ",
                 "/|   ",
                 "       "),
               4:("  o   ",
                 " /|\\ ",
                 "       "),
               5:(" o  ",
                 "/|\\ ", 
                 "/    ") ,
               6: (" o  ",
                 "/|\\", 
                 "/ \\") }

def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print("".join(answer))

def main():
    is_running = True
    answer = random.choice(words)
    guesses_made = 0
    wrong_guesses = 0
    guessed_letter = set()
    hint = ["_"] * len(answer) 
    print("*** PYTHON HANGMAN GAME! ***")
    while is_running:
        print("****************")
        display_man(wrong_guesses)
        print("****************")
        display_hint(hint)
        guess = input("Enter a letter:").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input!")
            continue
        
        if guess in guessed_letter:
            print(f" {guess} is already guessed")
            continue

        guessed_letter.add(guess)
        guesses_made += 1
    

        if guess in answer:
            for index in range(len(answer)):
                if answer[index] == guess:
                    hint[index] = guess
            print("Correct Answer!🥳")            
        else:
            print("Incorrect answer!!😈")
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!🥳🥳")
            print(f"It took you {guesses_made} guess/s to do so :p")
            choice = input("Do u wish to play again?(Y/N):").upper()
            if choice not in ("Y" , "YES"):
               is_running = False
               print("Thanks for playing!Goodbye😊")
            else :
                answer = random.choice(words)
                guesses_made = 0
                wrong_guesses = 0
                guessed_letter.clear()
                hint = ["_"] * len(answer) 

        if wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!😞😞😞")
            choice = input("Do u wish to play again?(Y/N):").upper()
            if choice not in( "Y" , "YES"):
               is_running = False
               print("Thanks for playing!Goodbye😊")
            else:
             answer = random.choice(words)
             guesses_made = 0
             wrong_guesses = 0
             guessed_letter.clear()
             hint = ["_"] * len(answer) 


        
if __name__ == "__main__":
    main()