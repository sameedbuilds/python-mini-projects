questions = ("Which animal lays the biggest egg?: ",
             "Which planet is the hottest?: ",
             "How many bones are there in the human body?: ",
             "How many elements in the periodic table?: ",
             "Which is the most abundant gas in the atmospphere?: ")

options = (("A.Whale, B.Elephant , C.Ostrich , D.Hippopotamus ",
            "A.Mercury , B.Venus , C.Earth , D.Mars ",
            "A.206 , B.207 , C.208 , D.209 ",
            "A.116 , B.117 , C.118 , D.119 ",
            "A.Oxygen , B.Carbon-Dioxide , C.NItrogen , D.Helium "))
guesses = []
answers = ("C", "B" , "A" , "B" ,"C")
score = 0
question_num = 0


for question in questions:
    print("---------------")
    print(f"{question_num+1}. {question}")
    for option in options[question_num]:
        print(option , end = "")
    print()

    guess = input("Enter your answer(A , B , C , D):").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score +=1
        print (" ✅Correct!")
    else:
        print(f"❌INCORRECT!")
        print(f"The correct answer is: {answers[question_num]}‼️")
    question_num +=1
print()
print("-----RESULT-----")
print("The correct answers were: ")
for answer in answers:
    print(answer , end = " ")
print()
print("Your answers were:")
for guess in guesses:
    print(guess , end = " ")
print()
print(f"Therefore, your score is: {score}/{question_num}")
score2 = float((score / question_num) * 100)
print(f"Your percentage is {score2}%")
