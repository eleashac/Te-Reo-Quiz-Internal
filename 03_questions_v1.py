"""
Te Reo Quiz - Questions v1
set up 10 Te Reo Maori quiz questions
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
print("\nQuestion 3: What is 'mana' in Māori culture?\n"
      "\ta) Power and prestige\n"
      "\tb) Love and kindness\n"
      "\tc) Freedom and liberty\n")
answer = input("Your answer: ").lower()
if answer == "a":
    print("Correct! Mana is power, prestige, and authority -  the supernatural "
          "force in a person, place or object.")
    score += 1
else:
    print("Incorrect. The answer is a) mana, which means power, prestige, and "
          "authority - the supernatural force in a person, place or object.")


# Question 4
print("\nQuestion 4: What is the Māori word for goodbye?\n"
      "\ta) Aroha nui\n"
      "\tb) Kia ora\n"
      "\tc) Haere rā\n")
answer = input("Your answer: ").lower()
if answer == "c":
    print("Correct! Haere rā is used to say goodbye to somebody who is "
          "leaving while you're staying.")
    score += 1
else:
    print("Incorrect. The answer is c) haere rā, which is used to say goodbye "
          "to somebody who is leaving while you're staying.")


# Question 5
print("\nQuestion 5: What does 'waiata' translate to?\n"
      "\ta) Dance\n"
      "\tb) Song\n"
      "\tc) Story\n")
answer = input("Your answer: ").lower()
if answer == "b":
    print("Correct! Waiata is a Māori word for song or chant.")
    score += 1
else:
    print("Incorrect. Waiata is a Māori word for b) song or chant.")


# Question 6
print("\nQuestion 6: What is the Māori name for the NZ native silver fern?\n"
      "\ta) Kowhai\n"
      "\tb) Kahikatea\n"
      "\tc) Ponga\n")
answer = input("Your answer: ").lower()
if answer == "c":
    print("Correct! The silver fern is a national symbol of New Zealand and is "
          "known in Te Reo Māori as ponga.")
    score += 1
else:
    print("Incorrect. The silver fern is a national symbol of New Zealand and "
          "is known in Te Reo Māori as c) ponga.")


# Question 7
print("\nQuestion 7: What is a 'hongi' in Māori culture?\n"
      "\ta) A traditional Māori greeting\n"
      "\tb) A type of food\n"
      "\tc) A type of dance\n")
answer = input("Your answer: ").lower()
if answer == "a":
    print("Correct! A hongi is a traditional Māori greeting in which two people"
          " press their noses together to show the sharing of breath. It is a "
          "sign of peace and also a sign of life and well-being.")
    score += 1
else:
    print("Incorrect. A hongi is a) a traditional Māori greeting in which two "
          "people press their noses together to show the sharing of breath. It "
          "is a sign of peace and also a sign of life and well-being.")


# Question 8
print("\nQuestion 8: What is the meaning of 'tino rangatiratanga'?\n"
      "\ta) Honesty\n"
      "\tb) Respect\n"
      "\tc) Self-determination\n")
answer = input("Your answer: ").lower()
if answer == "c":
    print("Correct! Tino rangatiratanga is a Māori term meaning "
          "self-determination or autonomy.")
    score += 1
else:
    print("Incorrect. Tino rangatiratanga is a Māori term meaning "
          "c) self-determination or autonomy.")


# Question 9
print("\nQuestion 9: What is the Māori word for family?\n"
      "\ta) Whānau\n"
      "\tb) Kai\n"
      "\tc) Whenua\n")
answer = input("Your answer: ").lower()
if answer == "c":
    print("Correct! Whānau represents a broader sense of family, including "
          "extended family and close friends.")
    score += 1
else:
    print("Incorrect. Tino rangatiratanga is a Māori term meaning "
          "c) self-determination or autonomy.")


# Question 10
print("\nQuestion 10: How do you say love in Te Reo Māori?\n"
      "\ta) Aroha\n"
      "\tb) Mana\n"
      "\tc) Whenua\n")
answer = input("Your answer: ").lower()
if answer == "a":
    print("Correct! Aroha is the Māori word for love, compassion, and empathy.")
    score += 1
else:
    print("Incorrect. a) Aroha is the Māori word for love, compassion, and "
          "empathy.")

print(f"\nYour score: {score}")
