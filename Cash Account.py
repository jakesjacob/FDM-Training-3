cashAccount = 0


def depositCash(value):
    if value <= 500:
        cashAccount = cashAccount + value
    elif value > 500:
        print("The deposit limit is £500")
    elif value == 0:
        print("Please enter a value larger than 0")
    elif value < 0:
        print("Please enter a value larger than 0")
