import random
import time
import schedule
import cashAccount


shareMenuList = ("1", "2", "3")

investAccount = 0

share1 = float(1.0)
share2 = float(1.0)
share3 = float(1.0)

share1rounded = float(1.0)
share2rounded = float(1.0)
share3rounded = float(1.0)

share1List = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
share2List = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
share3List = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

share1Amount = 0
share2Amount = 0
share3Amount = 0

share1investValue = 0
share2investValue = 0
share3investValue = 0


def shiftLeft(sequence, shiftNum=0):
    shiftValue = shiftNum % len(sequence)
    return sequence[+shiftValue:] + sequence[:+shiftValue]


def shareShift():
    global share1List
    global share2List
    global share3List

    share1List = shiftLeft(share1List, 1)
    share1List[-1] = share1rounded

    share2List = shiftLeft(share2List, 1)
    share2List[-1] = share2rounded

    share3List = shiftLeft(share3List, 1)
    share3List[-1] = share3rounded


def updateShares():
    global share1
    global share2
    global share3
    global share1rounded
    global share2rounded
    global share3rounded
    if random.random() > 0.35:
        share1 = share1 + random.uniform(0.1, 0.6)
    else:
        share1 = share1 - random.uniform(0.1, 0.6)

    if random.random() > 0.45:
        share2 = share1 + random.uniform(0.1, 0.7)
    else:
        share2 = share1 - random.uniform(0.1, 0.7)

    if random.random() > 0.4:
        share3 = share3 + random.uniform(0.1, 0.8)
    else:
        share3 = share3 - random.uniform(0.1, 0.8)

    share1rounded = round(share1, 1)
    share2rounded = round(share2, 1)
    share3rounded = round(share3, 1)

    shareShift()


schedule.every(1).seconds.do(updateShares)


def updateAllShares():
    schedule.run_pending()


def calculateShareValue(sharePrice, shareAmount):
    shareValue = sharePrice * shareAmount
    return shareValue


def calculateTotalInvestAccount():
    updateAllShares()
    global share1Amount
    global share2Amount
    global share3Amount
    global investAccount
    global share1rounded
    global share2rounded
    global share3rounded
    global share1investValue
    global share2investValue
    global share3investValue

    share1investValue = calculateShareValue(share1rounded, share1Amount)
    share2investValue = calculateShareValue(share2rounded, share2Amount)
    share3investValue = calculateShareValue(share3rounded, share3Amount)

    investAccount = share1investValue + share2investValue + share3investValue


def viewPortfolioScreen():
    updateAllShares()
    global share1Amount
    global share2Amount
    global share3Amount
    calculateTotalInvestAccount()

    print("\nTotal Investing account is worth: £", investAccount)

    print("\nShare 1 amount of owned shares: ",
          share1Amount, "Worth: ", share1investValue)
    print("\nShare 2 amount of owned shares: ",
          share2Amount, "Worth: ", share2investValue)
    print("\nShare 3 amount of owned shares: ",
          share3Amount, "Worth: ", share3investValue)

    input("Press any key to retunr to Main Menu")


def displayShare1():
    global share1List
    count = 0
    print("\nViewing live prices of Share 1 for 5 seconds:\n")
    while count < 6:
        updateAllShares()
        #print("\n Update:\n")
        print(share1List, end="\r")
        count += 1
        time.sleep(1)


def displayShare2():
    global share2List
    count = 0
    print("\nViewing live prices of Share 2 for 5 seconds:\n")
    while count < 6:
        updateAllShares()
        #print("\n Update:\n")
        print(share2List, end="\r")
        count += 1
        time.sleep(1)


def displayShare3():
    global share3List
    count = 0
    print("\nViewing live prices of Share 3 for 5 seconds:\n")
    while count < 6:
        updateAllShares()
        #print("\n Update:\n")
        print(share3List, end="\r")
        count += 1
        time.sleep(1)


def buySharesScreen():
    updateAllShares()
    print("\nEnter which Share you would like to purchase or X to exit: ")
    shareNum = input("Share = ")
    buySharesInfo(shareNum)


def buySharesInfo(shareNum):
    updateAllShares()
    global share1Amount
    global share2Amount
    global share3Amount

    if shareNum in shareMenuList:
        if shareNum == "1":
            price = share1rounded
            print("Share ", shareNum, " price locked at: ", price)
            print("\nEnter the cash amount you want to invest: ")
            value = input("Amount = ")
            share1Amount = share1Amount + \
                buyShares(int(value), price)
            # print(share1Amount)
        elif shareNum == "2":
            price = share2rounded
            print("Share ", shareNum, " price locked at: ", price)
            print("\nEnter the cash amount you want to invest: ")
            value = input("Amount = ")
            share2Amount = share2Amount + \
                buyShares(int(value), price)
        elif shareNum == "3":
            price = share3rounded
            print("Share ", shareNum, " price locked at: ", price)
            print("\nEnter the cash amount you want to invest: ")
            value = input("Amount = ")
            share3Amount = share3Amount + \
                buyShares(int(value), price)
        elif shareNum == "X" or shareNum == "x":
            print("exit")
        else:
            print("Please enter a valid input")
            buySharesScreen()


def buyShares(value, price):
    if value <= cashAccount.cashAccount and value > 0:
        cashAccount.cashAccount = cashAccount.cashAccount - value
        shares = value/price
        sharesRounded = round(shares, 1)
        print("\nSUCCESS: You have purchased ", sharesRounded, " shares for £", value,
              ". \nReturning to the Main Menu please wait.")
    elif value > cashAccount.cashAccount:
        print("\nERROR!!! You don't have enough funds in you Cash Account. !!!ERROR. \nReturning to the Main Menu please wait.")
        sharesRounded = 0
    elif value <= 0:
        print("\nERROR!!! Please enter a value larger that 0. !!!ERROR. \nReturning to the Main Menu please wait.")
        sharesRounded = 0
    return sharesRounded


# def sellSharesScreen():
