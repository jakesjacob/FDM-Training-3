cashAccount = 0


def depositCash(value, cashAccount):
    if value <= 500 and value > 0:
        newCashAccount = cashAccount + value
    elif value > 500:
        print("ERROR!!! The deposit limit is £500. !!!ERROR")
        newCashAccount = cashAccount
    elif value == 0:
        print("ERROR!!! Please enter a value larger than 0. !!!ERROR")
        newCashAccount = cashAccount
    elif value < 0:
        print("ERROR!!! Please enter a value larger than 0. !!!ERROR")
        newCashAccount = cashAccount
    return newCashAccount


def withdrawCash(value, cashAccount):
    if value <= cashAccount and value > 0:
        newCashAccount = cashAccount - value
    elif value > cashAccount:
        print("ERROR!!! You don't have enough funds for that. !!!ERROR")
        newCashAccount = cashAccount
    elif value == 0:
        print("ERROR!!! please enter a value larger than 0. !!!ERROR")
        newCashAccount = cashAccount
    elif value < 0:
        print("ERROR!!! Please enter a value larger than 0. !!!ERROR")
        newCashAccount = cashAccount
    return newCashAccount


thisIsTrue = True

while thisIsTrue:
    print("\n\nYour Cash Account value = " + str(cashAccount))
    print("\nMenu")
    print("1 - Deposit\n2 - Withdraw")
    selection = input("Enter your selection: ")
    if selection == "1":
        print("\nEnter the amount you want to deposit: ")
        value = input("Amount = ")
        cashAccount = depositCash(int(value), cashAccount)
    elif selection == "2":
        print("\nEnter the amount you want to withdraw: ")
        value = input("Amount = ")
        cashAccount = withdrawCash(int(value), cashAccount)


def depositScreen():
