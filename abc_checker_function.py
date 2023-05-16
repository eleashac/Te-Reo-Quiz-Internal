"""
Te Reo Quiz - ABC Check
converts abc_checker_v1 into a function
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
