"""
Te Reo Quiz - Yes/No check v2
simplifies the input by converting it to lower case. Also accepts
y or n as abbreviations. Prints result of user choice and input - for testing
"""


# Ask user if they would like to read the instructions
show_instructions = input("Would you like to read the instructions? ").lower()

# If they say no, output 'Program Continues'
if show_instructions == "no" or show_instructions == "n":
    print("Program Continues")

# If they say yes, output 'Display instructions'
elif show_instructions == "yes" or show_instructions == "y":
    print("Display instructions")

# Otherwise, show error
else:
    print("Please enter yes or no")

print(f"You have entered {show_instructions}")
