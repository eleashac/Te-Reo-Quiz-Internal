"""
Te Reo Quiz - ABC Check
makes sure answer input is valid
"""


# while loop to ensure input is a, b, or c
while True:
    answer = input("Your answer: ").lower()
    if answer in ["a", "b", "c"]:
        break
    print("Please enter a, b, or c: ")
