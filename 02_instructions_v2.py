"""
Te Reo Quiz - User details and instructions
incorporates yes/no and instructions function
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

        # If they say yes, output 'Program Continues'
        else:
            answer = "No"
            return answer


# display instructions function
def instructions():
    print("\n***** Te Reo Quiz *****\n")
    print("The rules of the game will go here\n")
    print("Program Continues\n")


# get user details
user_name = input("What is your name? ").title()
user_age = int(input("How old are you? "))


# greet user and if under 9 years old warn it may be challenging
if user_age < 9:
    print(f"\nHi {user_name}! At {user_age} years old, these questions may be "
          f"challenging. Good luck!")
else:
    print(f"\nHi {user_name}!")


# main routine
want_instructions = yes_no("Would you like to read the instructions? ")

if want_instructions == "Yes":
    instructions()
else:
    print("Program Continues")
