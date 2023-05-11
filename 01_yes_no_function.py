"""
Lucky Unicorn - Yes/No check function
based on 01_yes_no_v3
Created by Eleasha Chan
"""


# yes/no check function
def yes_no(question_text):
    while True:

        # Ask user if they would like the instructions
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


# main routine
show_instructions = yes_no("Would you like to read the instructions? ")
print(f"You have entered {show_instructions}")
