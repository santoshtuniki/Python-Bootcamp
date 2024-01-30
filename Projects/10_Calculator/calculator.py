from art import logo

print(logo)


def add(n1, n2):
    return n1+n2


def subtract(n1, n2):
    return n1-n2


def multiply(n1, n2):
    return n1*n2


def divide(n1, n2):
    return n1/n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


num1 = int(input("What is your first number?\n"))
num2 = int(input("What is your second number?\n"))

for symbol in operations:
    print(symbol)

operation_symbol = int(input("Pick an operation symbol from the line above: "))

function = operations[operation_symbol]

answer = function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")
