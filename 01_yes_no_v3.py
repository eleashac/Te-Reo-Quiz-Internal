"""
Te Reo Quiz - Yes/No check v3
changes 01_yes_no_v2 into a while loop to keep asking user for input until they
reply either yes or no (yes, y, no, n).
Created by Eleasha Chan
"""


# Ask user if they would like the instructions
show_instructions = input("Would you like to read the instructions? ").lower()


while show_instructions != "yes" and show_instructions != "no" and \
        show_instructions != "y" and show_instructions != "n":
    print("Please enter yes or no")

    show_instructions = input("Would you like to read the instructions? ")\
        .lower()

# If they say no, output 'Program Continues'
if show_instructions == "no" or show_instructions == "n":
    print("Program Continues")

# If they say no, output 'Display instructions'
else:
    print("Display instructions")
