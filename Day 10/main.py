import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

import art

def add(n1, n2):
    return n1+n2

def sub(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

operations = {
    "/":divide, "+":add, "-":sub, "*":multiply
    }

def calculator():
    print(art.logo)
    def calculation(num1, num2):
        function_call = operations[operation_symbol]
        return function_call(num1, num2)

    num1 = float(input("What is the first number?"))
    for symbol in operations:
        print(symbol)
    operation_symbol =input("Pick an operation from the line above: ") 
    num2 = float(input("What is the second number?"))

    answer = calculation(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    zero = 0
    while zero == 0:
        restart = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start anew.")
        if restart == "y":
            print("*"*30)
            num1 = answer
            for symbol in operations:
                print(symbol)
            operation_symbol =input("Pick an operation from the line above: ")
            num2 = float(input("What is the next number?"))
            answer = calculation(num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {answer}")
        else:
            cls()
            zero += 1
            calculator()
calculator()