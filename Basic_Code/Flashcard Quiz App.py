flashcards = {
    "Capital of France?": "Paris",
    "5 + 7 = ?": "12",
    "Python is a...": "Programming Language",
    "Gowtham G.s Patil...": "Data Analyst"
}

for question, answer in flashcards.items():
    user_answer = input(f"{question} ")
    if user_answer.strip().lower() == answer.lower():
        print("Correct!\n")
    else:
        print(f"Wrong! The correct answer is {answer}\n")
