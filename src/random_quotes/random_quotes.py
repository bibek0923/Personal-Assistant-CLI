
"""
6. Random Quotes Generator
● Store a list of motivational quotes in a file.
● Display a random quote whenever the user requests one

"""
import random

def random_quote():
    # Predefined list of quotes
    quotes = [
        "The best way to predict the future is to create it.",
        "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "Believe you can and you're halfway there.",
        "The only limit to our realization of tomorrow will be our doubts of today.",
        "Don't watch the clock; do what it does. Keep going.",
        "Act as if what you do makes a difference. It does."
    ]
    
    # Display a rand_quot
    if quotes:
        print("Here's your motivational quote:")
        print(random.choice(quotes))
    else:
        print("No quotes available.")

# Call the function
random_quote()
