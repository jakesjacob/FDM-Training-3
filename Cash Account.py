cashAccount = 0


def depositCash(value, cashAccount):
    if value <= 500:
        newCashAccount = cashAccount + value
    elif value > 500:
        print("The deposit limit is £500")
    elif value == 0:
        print("Please enter a value larger than 0")
    elif value < 0:
        print("Please enter a value larger than 0")
    return newCashAccount


thisIsTrue = True

while thisIsTrue:
    #cashAccount = 0
    print("Your Cash Account value = " + str(cashAccount))
    print(cashAccount)
    print("Menu")
    print("1 - Deposit")
    if input("Press 1 for Deposits") == "1":
        print("Enter the amount you want to deposit: ")
        value = input("Amount = ")
        cashAccount = depositCash(int(value), cashAccount)
