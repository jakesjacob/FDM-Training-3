

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


while 1:
    fizzBuzz()
