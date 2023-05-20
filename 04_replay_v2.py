"""
Te Reo Quiz - Replay
adds goodbye message when user doesn't play again
"""


# abc checker function
def a_b_c():
    while True:
        _answer = input("Your answer: ").lower()
        if _answer in ["a", "b", "c"]:
            return _answer
        print("Please enter a, b, or c")


# Define the list of questions and answers
questions = [
    {
        'question': "What is the Māori word for water?",
        'options': ['a) Wai', 'b) Āhua', 'c) Whenua'],
        'answer': 'a',
        'explanation': "The Māori word for water is 'wai'."
    },
    {
        'question': "What is the Māori name for New Zealand?",
        'options': ['a) Whakapapa', 'b) Aotearoa', 'c) Hīkoi'],
        'answer': 'b',
        'explanation': "Aotearoa translates to 'Land of the Long White Cloud' "
                       "in English."
    },
    {
        'question': "What is 'mana' in Māori culture?",
        'options': ['a) Power and prestige', 'b) Love and kindness',
                    'c) Freedom and liberty'],
        'answer': 'a',
        'explanation': "Mana is power, prestige, and authority - the "
                       "supernatural force in a person, place, or object."
    },
    {
        'question': "What is the Māori word for goodbye?",
        'options': ['a) Aroha nui', 'b) Kia ora', 'c) Haere rā'],
        'answer': 'c',
        'explanation': "Haere rā is used to say goodbye to somebody who is "
                       "leaving while you're staying."
    },
    {
        'question': "What does 'waiata' translate to?",
        'options': ['a) Dance', 'b) Song', 'c) Story'],
        'answer': 'b',
        'explanation': "Waiata is a Māori word for song or chant."
    },
    {
        'question': "What is the Māori name for the NZ native silver fern?",
        'options': ['a) Kowhai', 'b) Kahikatea', 'c) Ponga'],
        'answer': 'c',
        'explanation': "The silver fern is a national symbol of New Zealand "
                       "and is known in Te Reo Māori as ponga."
    },
    {
        'question': "What is a 'hongi' in Māori culture?",
        'options': ['a) A traditional Māori greeting', 'b) A type of food',
                    'c) A type of dance'],
        'answer': 'a',
        'explanation': "A hongi is a traditional Māori greeting in which two "
                       "people press their noses together to show the sharing "
                       "of breath. It is a sign of peace and also a sign of "
                       "life and well-being."
    },
    {
        'question': "What is the meaning of 'tino rangatiratanga'?",
        'options': ['a) Honesty', 'b) Respect', 'c) Self-determination'],
        'answer': 'c',
        'explanation': "Tino rangatiratanga is a Māori term meaning "
                       "self-determination or autonomy."
    },
    {
        'question': "What is the Māori word for family?",
        'options': ['a) Whānau', 'b) Kai', 'c) Whenua'],
        'answer': 'a',
        'explanation': "Whānau represents a broader sense of family, including "
                       "extended family and close friends."
    },
    {
        'question': "How do you say love in Te Reo Māori?",
        'options': ['a) Aroha', 'b) Mana', 'c) Whenua'],
        'answer': 'a',
        'explanation': "Aroha is the Māori word for love, compassion, and "
                       "empathy."
    }
]


# Function to play the quiz
def play_quiz():

    # Initialize score
    score = 0

    # Iterate over each question in the list
    for question_number in range(len(questions)):
        question = questions[question_number]

        # Adds one each time to get question numbers that increase each round
        print(f"\nQuestion {question_number + 1}: {question['question']}")

        # prints options (a, b, c) for question
        for option in question['options']:
            print(option)

        # main routine for abc checker to ensure user inputs valid answer
        user_answer = a_b_c()

        # tell user if they are correct or incorrect and provide short,
        # informative explanation of quiz word
        if user_answer == question['answer']:
            print("Correct!", question['explanation'])
            score += 1
        else:
            print("Incorrect.", question['explanation'])

    # Print the final score out of the total amount of questions
    print(f"\nYour score: {score}/{len(questions)}")

    # Ask if the user wants to play again
    play_again = input("Would you like to play again? (yes/no): ")

    # if 'yes', replay quiz questions
    if play_again == "yes" or play_again == "y":
        play_quiz()

    # if anything else, display goodbye message
    else:
        print("\nThank you for playing! Ka kite anō!")


# Start the quiz
play_quiz()
