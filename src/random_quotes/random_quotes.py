
"""
6. Random Quotes Generator
● Store a list of motivational quotes in a file.
● Display a random quote whenever the user requests one

"""
import random
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def random_quote():
    with open(os.path.join(ROOT_DIR, 'quotes.txt')) as f:
        quotes = f.read().split('\n')
    
    # Predefined list of quotes
    # quotes = [
    #     "The best way to predict the future is to create it.",
    #     "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    #     "Believe you can and you're halfway there.",
    #     "The only limit to our realization of tomorrow will be our doubts of today.",
    #     "Don't watch the clock; do what it does. Keep going.",
    #     "Act as if what you do makes a difference. It does."
    # ]
    
    # Display a rand_quot
    if quotes:
        print("Here's your motivational quote:")
        print(random.choice(quotes))
    else:
        print("No quotes available.")

def quote_menu() -> int:
    print("-------------------------------------------")
    print("Welcome to Random Quotes")
    print("Select from options below:")
    print("-------------------------------------------")
    print("1. Show Random Quotes")
    print("-------------------------------------------")
    print("Press any key to exit")
    print("-------------------------------------------")
    try: 
        return int(input("Enter option : "))
    except Exception as e:
        return 0

def start():
    try:
        option = 1
        while(option):
            option = quote_menu()
            if (option == 1):
                print('\n')
                random_quote()
            else:
                print("\nExiting...")
    except Exception as e:
        print(e)

start()