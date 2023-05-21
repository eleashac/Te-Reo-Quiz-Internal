"""
Te Reo Quiz - User details and instructions
increases age to under 11 for 'challenging' warning
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
def integer_checker(question):
    error = "\nSorry, you must enter an integer"
    age = ""
    while not age:
        try:
            age = int(input(question))
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


# get user details
user_name = input("What is your name? ").title()
user_age = integer_checker("How old are you? ")


# greet user and if under 11 years old warn it may be challenging
if user_age < 11:
    print(f"\nKia ora {user_name}! At {user_age} years old, these questions "
          f"may be challenging. Good luck!")
else:
    print(f"\nKia ora {user_name}!")


# main routine
want_instructions = yes_no("Would you like to read the instructions? ")

if want_instructions == "Yes":
    instructions()
else:
    print("Program Continues")
