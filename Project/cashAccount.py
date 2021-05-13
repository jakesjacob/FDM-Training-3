cashAccount = 200


def depositCash(value, cashAccount):
    if value <= 500 and value > 0:
        newCashAccount = cashAccount + value
        print("\nSUCCESS: You have deposited £" + str(value) +
              ". \nReturning to the Main Menu please wait.")
    elif value > 500:
        print("\nERROR!!! The deposit limit is £500. !!!ERROR. \nReturning to the Main Menu please wait.")
        newCashAccount = cashAccount
    elif value == 0:
        print("\nERROR!!! Please enter a value larger than 0. !!!ERROR. \nReturning to the Main Menu please wait.")
        newCashAccount = cashAccount
    elif value < 0:
        print("\nERROR!!! Please enter a value larger than 0. !!!ERROR. \nReturning to the Main Menu please wait.")
        newCashAccount = cashAccount
    return newCashAccount


def withdrawCash(value, cashAccount):
    if value <= cashAccount and value > 0:
        newCashAccount = cashAccount - value
        print("\nSUCCESS: You have withdrawn £" + str(value) +
              ". \nReturning to the Main Menu please wait.")
    elif value > cashAccount:
        print("\nERROR!!! You don't have enough funds for that. !!!ERROR. \nReturning to the Main Menu please wait.")
        newCashAccount = cashAccount
    elif value == 0:
        print("\nERROR!!! please enter a value larger than 0. !!!ERROR. \nReturning to the Main Menu please wait.")
        newCashAccount = cashAccount
    elif value < 0:
        print("\nERROR!!! Please enter a value larger than 0. !!!ERROR. \nReturning to the Main Menu please wait.")
        newCashAccount = cashAccount
    return newCashAccount


def depositScreen():
    global cashAccount
    print("\nEnter the amount you want to deposit: ")
    value = input("Amount = ")
    cashAccount = depositCash(int(value), cashAccount)


def withdrawScreen():
    global cashAccount
    print("\nEnter the amount you want to withdraw: ")
    value = input("Amount = ")
    cashAccount = withdrawCash(int(value), cashAccount)
