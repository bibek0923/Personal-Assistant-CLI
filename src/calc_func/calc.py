"""

5. Calculator
● Provide basic calculator functionality (addition, subtraction, multiplication, division).
● Include input validation and error handling (e.g., divide by zero).
"""
def calculator():
    try:
        num1=int(input("Input the first number:"))
        operator= input("Input an operator(*,+,-,/)")
        num2= int(input("Input the second number:"))

        if operator == "+":
            print(f"Result: {num1 +num2}")
        
        elif operator == "-":
            print(f"Result:{num1-num2}")
        
        elif operator == "*":
            print(f"Result:{num1*num2}")
        
        elif operator == "/":
            if num2!=0:
                print(f"Result:{num1/num2}")
        
        else :
            print("Invalid Operator:")
    except ValueError:
        print("Invalid input.Please enter numbers only")
# calculator()

def calculator_menu() -> int:
    print("-------------------------------------------")
    print("Welcome to Calculator")
    print("Select from options below:")
    print("-------------------------------------------")
    print("1. Start")
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
            option = calculator_menu()
            if (option == 1):
                calculator()
            else:
                print("\nExiting...")
    except Exception as e:
        print(e)