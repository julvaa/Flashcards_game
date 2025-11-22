import random
print("FLASHCARD QUIZ GAME")
print("Add questions. Type 'done' when finished.\n")

flashcards = []

while True:
    question = input("Enter a question (or 'done' to finish): ").strip()
    if question.lower() == "done":
        break
    answer = input("Enter the answer: ").strip()

    flashcards.append((question, answer))
    with open("flashcards.txt", "a", encoding="utf-8") as f:
        f.write(question + "-->" + answer + "\n")

    print("Flashcard added to file \n")

while True:

    print("\nLet's start the quiz. If you want to leave type exit")
    score = 0

    shuffled = flashcards[:]
    random.shuffle(shuffled)

    for question, answer in shuffled:
        print("\nQuestion:", question)
        user_answer = input("Your answer: ").strip()

        if user_answer.lower() == "exit":
            exit_pr = True
            break

        if user_answer.lower() == answer.lower():
            print(" Correct answer")
            score += 1
        else:
            print("Wrong. The correct answer is: ", answer)

        if exit_pr:
            print("\nExiting quiz.")
            break

    print("\nQuiz complete!")
    print(f"You got {score} out of {len(flashcards)} correct.")


