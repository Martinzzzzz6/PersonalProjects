from replit import clear

def multiplication(a, b):
    return a * b   

def division(a, b):
    return a / b

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def exponentiation(a, b):
    return a ** b

operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
    "^": exponentiation,
}

num1 = int(input("What's the first number? "))

for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number? "))

function = operations[operation_symbol]
answer = function(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")

should_continue = True
while should_continue:
    should_we_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to quit: ")
    if should_we_continue == 'n':
        should_continue = False
        break
    else:
        operation_symbol =  input("Pick another operation: ")
        num3 = int(input("What's the next number? "))
        function = operations[operation_symbol]
        previous_answer = answer
        answer = function(answer, num3)
        print(f"{previous_answer} {operation_symbol} {num3} = {answer}")
