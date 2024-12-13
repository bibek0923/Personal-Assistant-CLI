"""

5. Calculator
● Provide basic calculator functionality (addition, subtraction, multiplication, division).
● Include input validation and error handling (e.g., divide by zero).
"""
def calculator():
    try:
        print("Welcome to Calculator")
        print("-------------------------------------------")
        
        print("Enter the type of operation :")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Division")
        print("4. Multiplication")
        print("5. Exit")
        
        
        option=int(input("Enter option: "))
        match option:
            case 1: 
                num1=int(input("Input the first number:"))
                num2= int(input("Input the second number:"))
                print(f"Result: {num1 +num2}")
            
            case 2: 
                num1=int(input("Input the first number:"))
                num2= int(input("Input the second number:"))
                print(f"Result:{num1-num2}")
            
            case 3: 
                num1=int(input("Input the first number:"))
                num2= int(input("Input the second number:"))
                if num2!=0:
                    print(f"Result:{num1/num2}")
                else :
                    print("Enter valid second number")
            case 4 :
                num1=int(input("Input the first number:"))
                num2= int(input("Input the second number:"))
                print(num1*num2)
                
            case 5:
                exit
        # num1=int(input("Input the first number:"))
        # operator= input("Input an operator(*,+,-,/)")
        # num2= int(input("Input the second number:"))
        
        # if operator == "+":
        #     print(f"Result: {num1 +num2}")
        
        # elif operator == "-":
        #     print(f"Result:{num1-num2}")
        
        # elif operator == "*":
        #     print(f"Result:{num1*num2}")
        
        # elif operator == "/":
        #     if num2!=0:
        #         print(f"Result:{num1/num2}")
        
        # else :
        #     print("Invalid Operator:")
    except ValueError:
        print("Invalid input.Please enter numbers only")
# calculator()

# def calculator_menu() -> int:
#     print("-------------------------------------------")
#     print("Welcome to Calculator")
#     print("Select from options below:")
#     print("-------------------------------------------")
#     print("1. Start")
#     print("-------------------------------------------")
#     print("Press any key to exit")
#     print("-------------------------------------------")
#     try: 
#         return int(input("Enter option : "))
#     except Exception as e:
#         return 0

def start():
    try:
        # option = 1
        # while(option):
        #     calculator_menu()
        #     if (option == 1):
        #         calculator()
        #     else:
        #         print("\nExiting...")
        calculator()
    except Exception as e:
        print(e)



    