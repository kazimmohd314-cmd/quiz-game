# ------------------------------
#   QUIZ GAME PROJECT IN PYTHON
# ------------------------------

# Function to display a single question
def ask_question(question, options, correct_answer):
    print("\n" + question)
    for opt in options:
        print(opt)
    answer = input("Enter your answer (a/b/c/d): ").lower()

    if answer == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"Wrong! Correct answer is: {correct_answer}")
        return False


# Main Quiz Function
def start_quiz():
    print("\n===== WELCOME TO THE PYTHON QUIZ GAME =====\n")
    score = 0

    # List of questions with options and answers
    quiz = [
        {
            "question": "Who developed Python programming language?",
            "options": ["a) Elon Musk", "b) Dennis Ritchie", "c) Guido van Rossum", "d) James Gosling"],
            "answer": "c"
        },
        {
            "question": "Which keyword is used to create a function in Python?",
            "options": ["a) func", "b) define", "c) def", "d) function"],
            "answer": "c"
        },
        {
            "question": "Which of the following data structures is mutable?",
            "options": ["a) Tuple", "b) String", "c) List", "d) Integer"],
            "answer": "c"
        },
        {
            "question": "Which operator is used for exponent (power) in Python?",
            "options": ["a) ^", "b) **", "c) *", "d) //"],
            "answer": "b"
        },
        {
            "question": "What is the correct file extension for Python programs?",
            "options": ["a) .pt", "b) .p", "c) .py", "d) .python"],
            "answer": "c"
        }
    ]

    # Loop through all questions
    for q in quiz:
        if ask_question(q["question"], q["options"], q["answer"]):
            score += 1

    # Final result
    print("\n===== QUIZ FINISHED =====")
    print(f"Your Final Score: {score}/{len(quiz)}")

    # Score evaluation
    if score == len(quiz):
        print("Excellent! Full marks 👏🔥")
    elif score >= len(quiz) - 2:
        print("Great job! 😄")
    elif score >= len(quiz) // 2:
        print("Good effort! Keep practicing 👍")
    else:
        print("Needs improvement. Try again! 💪")


# Start the program
start_quiz()
