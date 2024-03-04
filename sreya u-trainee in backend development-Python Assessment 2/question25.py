"""25.Quiz Game in Python"""

questions = ("how many elements are there in the periodic table?:",
             "which animal lays the largest eggs?:",
             "How many bones are there in the human body?:",
             "which planet in the solar system is the hottest?:")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon Dioxide", "D. Hydrogen"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("A", "B", "A", "B")

guesses = []
score = 0

for question_num, question in enumerate(questions):
    print("--------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"The correct answer is: {answers[question_num]}")

total_questions = len(questions)
percentage_score = (score / total_questions) * 100

print("____________")
print("Results")
print("____________")

print("Answers:", end=" ")
for ans in answers:
    print(ans, end=" ")
print()

print(f"Your score is: {percentage_score}%")
