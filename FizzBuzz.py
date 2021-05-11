

def fizzBuzz():
    userInput = input("Please enter a number: ")
    userInputInt = int(userInput)

    divide3 = userInputInt/3
    divide3int = int(divide3)

    divide5 = userInputInt/5
    divide5int = int(divide5)

    if divide3 == divide3int and divide5 == divide5int:
        print("FIZZ BUZZ")
    elif divide3 == divide3int:
        print("FIZZ")
    elif divide5 == divide5int:
        print("BUZZ")
    else:
        print(userInput)


def fizzBuzz2():
    userInput = input("Please enter a number: ")
    userInputInt = int(userInput)

    if userInputInt % 3 == 0 and userInputInt % 5 == 0:
        print("FIZZ BUZZ")
    elif userInputInt % 3 == 0:
        print("FIZZ")
    elif userInputInt % 5 == 0:
        print("BUZZ")
    else:
        print(userInput)


while 1:
    fizzBuzz2()
