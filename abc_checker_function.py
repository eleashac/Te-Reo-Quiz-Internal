"""
Te Reo Quiz - ABC Checker
"""


# function to ensure input is a, b, or c
def a_b_c():
    while True:
        _answer = input("Your answer: ").lower()
        if _answer in ["a", "b", "c"]:
            return _answer
        print("Please enter a, b, or c.")


# main routine
answer = a_b_c()
