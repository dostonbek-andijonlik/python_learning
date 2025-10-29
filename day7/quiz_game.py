# Python quiz game

questions = ("What is the only planet in our solar system that rotates clockwise?: ",
             "A farmer has 17 sheep, and all but 9 run away. How many are left?: ",
             "Who wrote the famous novel 1984?: ",
             "What is the smallest prime number?: ",
             "What is the main ingredient in traditional hummus?: "
             )

options = (("A. Mars", "B. Jupiter", "C. Venus", "D: Mercury"), 
           ("A. 8", "B. 9", "C. 17", "D: 0"), 
           ("A. Aldous Huxley", "B. George Orwell", "C. Ernest Hemingway", "D: J.K. Rowling"), 
           ("A. 1", "B. 2", "C. 3", "D: 0"), 
           ("A. Lentils", "B. Chickpeas", "C. Peas", "D: Soybeans")) 
answers = ("C", "B", "B", "B", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer!")
    question_num += 1

print("---------------------------")
print("           RESULT          ")
print("---------------------------")

print("answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")