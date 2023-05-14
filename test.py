import random

# Define a list of tuples, where each tuple contains a question, three possible
# answers, and the index of the correct answer
questions = [
    ("What is the Māori word for hello?",
     ["1. Kia ora", "2. Haere rā", "3. Aroha"], 0),
    ("What is the Māori word for goodbye?",
     ["1. Haere rā", "2. Kia ora", "3. Aroha"], 0),
    ("What is the Māori word for thank you?",
     ["1. Kia ora", "2. Haere rā", "3. Aroha"], 0),
    ("What is the Māori word for please?",
     ["1. Whakarongo mai", "2. Haere rā", "3. Aroha"], 0),
    ("What is the Māori word for yes?", ["1. Āe", "2. Kāo", "3. Haere rā"], 0),
    ("What is the Māori word for no?", ["1. Kāo", "2. Āe", "3. Kia ora"], 0),
    ("What is the Māori word for love?",
     ["1. Aroha", "2. Kia ora", "3. Haere rā"], 0),
]

# Print instructions for the user
print("Kia ora! Welcome to the te reo Māori quiz.\n")
print(
    "Choose the correct answer by inputting the corresponding integer (1, 2, or 3) for each question.\n")

# Shuffle the order of the questions
random.shuffle(questions)

# Keep track of the number of correct answers
score = 0

# Loop through each question and ask the user for an answer
for q, a, c in questions:
    print(q)
    for ans in a:
        print(ans)

    # Keep asking for user input until a valid integer choice is made (1, 2, or 3)
    while True:
        try:
            ans = int(input("Your answer (input 1, 2, or 3): "))
            if ans not in [1, 2, 3]:
                raise ValueError
            break
        except ValueError:
            print(
                "Invalid input. Please input a valid integer choice (1, 2, or 3).\n")

    if ans == c + 1:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is:", a[c])
    print()  # Add a blank line for readability

# Print the final score
print("You got", score, "out of", len(questions), "questions correct.")
