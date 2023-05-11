"""
Te Reo Quiz - Yes/No check v1
"""

# Ask user if they would like to read the instructions
show_instructions = input("Would you like to read the instructions? ")

# If they say no, output 'Program Continues'
if show_instructions == "no":
    print("Program Continues")

# If they say yes, output 'Display instructions'
elif show_instructions == "yes":
    print("Display instructions")

# Otherwise, show error
else:
    print("Please enter yes or no")