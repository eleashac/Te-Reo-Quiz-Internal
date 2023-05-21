"""
Te Reo Quiz - Statement Formatter v1
example of use
"""


# function to format text output
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# main routine
print(formatter("*", "Welcome to the Te Reo Māori Quiz"))
print()
print(formatter("*", "Tino pai! You got a perfect score!"))
print()
print(formatter("=", "Thank you for playing! Ka kite anō!"))
