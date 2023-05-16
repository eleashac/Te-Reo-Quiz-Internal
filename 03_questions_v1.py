"""
Te Reo Quiz - Questions
set up 10 Te Reo Maori quiz questions
Created by Eleasha Chan
"""


# Initialize score
score = 0


# Question 1
print("\nQuestion 1: What is the Māori word for water?\n"
      "\ta) Wai\n"
      "\tb) Āhua\n"
      "\tc) Whenua\n")
answer = input("Your answer: ").lower()
if answer == "a":
    print("Correct! The Māori word for water is 'wai'.")
    score += 1
else:
    print("Incorrect. The correct answer is a) Wai.")


# Question 2
print("\nQuestion 2: What is the Māori name for New Zealand?\n"
      "\ta) Whakapapa\n"
      "\tb) Aotearoa\n"
      "\tc) Hīkoi\n")
answer = input("Your answer: ").lower()
if answer == "b":
    print("Correct! Aotearoa translates to 'Land of the Long White Cloud' "
          "in English.")
    score += 1
else:
    print("Incorrect. The answer is b) Aotearoa, which translates to the "
          "'Land of the Long White Cloud' in English.")


# Question 3
print("\nQuestion 2: What is 'mana' in Māori culture?\n"
      "\ta) Power and prestige\n"
      "\tb) Love and kindness\n"
      "\tc) Freedom and liberty\n")
answer = input("Your answer: ").lower()
if answer == "b":
    print("Correct! Mana translates to power, prestige, and authority")
    score += 1
else:
    print("Incorrect. The answer is a) mana, which means power, prestige, and "
          "authority.")



print(score)
