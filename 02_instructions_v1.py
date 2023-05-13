"""
Te Reo Quiz - User details and instructions
get user's name and age to address them
Created by Eleasha Chan
"""

# get user details
user_name = input("What is your name? ").title()
user_age = int(input("How old are you? "))

# main routine
if user_age < 9:
    print(f"\nHi {user_name}! At {user_age} years old, the questions may be "
          f"challenging.")

else:
    print(f"\nHi {user_name}!")
