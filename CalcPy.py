#!/usr/bin/python3
"""
CalcPy
Copyright: Juan Antonio Gil Chamorro (M4luk0)
"""

print("Welcome to calcpy!, a simple calculator made in python.")

fileName = input("\nFirst of all, select a name for the history archive; press Enter if you want history.txt: ")
if fileName == "":
    file = open("/home/m4luk0/PycharmProjects/Calculator/history.txt", "a+")
    fileName = "/home/m4luk0/PycharmProjects/Calculator/history.txt"
    file.close()
else:
    file = open("/home/m4luk0/PycharmProjects/Calculator/" + fileName, "a+")
    file.close()


def writeFile(operationResult):
    file = open(fileName, "a+")
    file.write(operationResult + "\n")
    file.close()


def add(a, b):
    result = float(a) + float(b)
    writeFile(a + " + " + b + " = " + str(result))
    return "El resultado es: ", result


def subtract(a, b):
    result = float(a) - float(b)
    writeFile(a + " - " + b + " = " + str(result))
    return "El resultado es: ", result


def multiply(a, b):
    result = float(a) * float(b)
    writeFile(a + " * " + b + " = " + str(result))
    return "El resultado es: ", result


def split(a, b):
    result = float(a) / float(b)
    writeFile(a + " / " + b + " = " + str(result))
    return "El resultado es: ", result


def exponential(a, b):
    reps = 0
    result = float(a)
    while reps < float(b):
        result = result * float(a)
        reps = reps + 1
    writeFile(a + " ^ " + b + " = " + str(result))
    return "El resultado es: ", result


def startProgram():
    print("What do you want to do? Select an option\nread) read history.\noperate) make an operation.")
    option = input("Type one of the options: ")
    if option == "read":
        linesToRead = input("Enter how much lines do you want to read: ")
        if linesToRead.isdigit():
            actualLine = 0
            file = open(fileName, "r")
            for line in file:
                print(line)
                actualLine = actualLine + 1
                if actualLine == int(linesToRead):
                    break
            file.close()
        else:
            print("You have to introduce a number!")
    elif option == "operate":
        print(
            "\nNow, what type of operation do you want to do?\n+) add\n-) subtract\n*) multiply\n/) split\n^) "
            "exponential")
        operation = input("Select an option: ")
        number1 = input("Perfect! now introduce the first number: ")
        number2 = input("OK, now the second one: ")
        if len(number1) > 10 or len(number2) > 10:
            print("You number is too long! you can't introduce more than ten digits!")
        else:
            if (number1.isdigit() or number1.lstrip("-").isdigit()) and (number2.isdigit() or number2.lstrip("-").isdigit()):
                if operation == "+":
                    print(add(number1, number2))

                elif operation == "-":
                    print(subtract(number1, number2))

                elif operation == "*":
                    print(multiply(number1, number2))

                elif operation == "/":
                    if float(number2) == 0.0:
                        print("You can't divide by zero!")
                        startProgram()
                    else:
                        print(split(number1, number2))

                elif operation == "^":
                    print(exponential(number1, number2))

                else:
                    print("Enter a valid operation!")
            else:
                print("You have to enter numbers!")
    else:
        print("Select a valid option!")

    while True:
        restart = input("Do you want to make another thing? (Type yes or no): ")
        if restart == "yes":
            startProgram()
            break
        elif restart == "no":
            break
        else:
            print("Select a valid option!")
            pass


startProgram()
