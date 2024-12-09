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
calculator()