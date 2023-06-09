"""
Te Reo Quiz - Base
components added after they have been created and tested
Created by Eleasha Chan
"""


# yes/no check function
def yes_no(question_text):
    while True:

        # Ask user if they want to read the instructions
        answer = input(question_text).lower()

        while answer != "yes" and answer != "no" and \
                answer != "y" and answer != "n":
            print("Please enter yes or no ")

            answer = input(question_text).lower()

        # If they say yes, output 'Display instructions'
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If they say no, output 'Program Continues'
        else:
            answer = "No"
            return answer


# integer check function
def integer_checker(question_):
    error = "\nSorry, you must enter an integer"
    age = ""
    while not age:
        try:
            age = int(input(question_))
            return age
        except ValueError:
            print(error)


# display instructions function
def instructions():
    print("\n***** Te Reo Quiz ***** \n")
    print("1. Press <enter> to begin. \n"
          "2. Type in the correct translation out of the options provided: "
          "either a, b, or c. \n"
          "3. Press <enter> to submit your answer and get the "
          "results of the round, and again to move onto the next question. \n"
          "\tAfter 10 rounds your final score will be displayed and you will "
          "get the option to play again. Kia Ora!")


# abc checker function
def a_b_c():
    while True:
        _answer = input("Your answer: ").lower()
        if _answer in ["a", "b", "c"]:
            return _answer
        print("Please enter a, b, or c")


# get user details
user_name = input("What is your name? ").title()
user_age = integer_checker("How old are you? ")


# greet user and if under 9 years old warn it may be challenging
if user_age < 9:
    print(f"\nTēnā koe {user_name}! At {user_age} years old, these questions "
          f"may be challenging. Good luck!")
else:
    print(f"\nKia ora {user_name}!")


# ask user if they want to read the instructions
want_instructions = yes_no("Would you like to read the instructions? ")

# if user inputs 'yes', show instructions
if want_instructions == "Yes":
    instructions()
    print()

# get user to press enter to play to prevent questions from displaying
# together with the instructions
print(input("Please press enter to start:"))

# Initialize score
score = 0


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

    # tell user if they are correct or incorrect and provide short, informative
    # explanation of quiz word
    if user_answer == question['answer']:
        print("Correct!", question['explanation'])
        score += 1
    else:
        print("Incorrect.", question['explanation'])


# Print the final score out of total amount of questions
print(f"\nYour score: {score}/{len(questions)}")
