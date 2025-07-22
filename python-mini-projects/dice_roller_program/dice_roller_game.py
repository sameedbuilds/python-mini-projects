import random
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# print("● ┌ ─ ┐ │ └ ┘")

#"┌─────────┐"
#"│         │"
#"│         │"
#"│         │"
#"└─────────┘"





dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),
        
    6: ("┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘")
    }

dice = []
total = 0

call = int(input("How many dice do u want?: "))
for die in range(call):
    dice.append(random.randint(1,6))

# for printing dices in consective lines
#for die in range(call):
#    for value in dice_art.get(dice[die]):
#        print(value)

# for printing dices in same line
for line_num in range(5):
    for rolled_value in dice:
        print(dice_art.get(rolled_value)[line_num] , end = "")
    print()
    
for die in dice:
    total += die
print(f"you rolled {dice}")
print(f"Total is: {total}")