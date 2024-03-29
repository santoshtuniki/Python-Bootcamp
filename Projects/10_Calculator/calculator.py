from art import logo


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


def calculator():

    print(logo)

    num1 = float(input("What's your first number?\n"))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:

        operation_symbol = input("Pick an operation: ")

        num2 = float(input("What's the next number?\n"))

        function = operations[operation_symbol]

        answer = function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(
            f"Type 'y' to continue calculating with {answer},\nType 'n' to start a new calculation,\nType 'q' to exit calculator:\t"
        ).lower()

        if choice == 'q':
            return
        elif choice == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
print('GoodBye!!!')