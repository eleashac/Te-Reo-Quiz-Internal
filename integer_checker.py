"""
Te Reo Quiz - Integer Checker
"""


# integer check function
def integer_checker(question):
    error = "\nSorry, you must enter an integer\n"
    age = ""
    while not age:
        try:
            age = int(input(question))
            return age
        except ValueError:
            print(error)


# main routine
user_age = integer_checker("How old are you? ")
