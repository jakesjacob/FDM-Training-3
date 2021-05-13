import menus
import shares
import cashAccount
import database as db


import os
from art import *
import pyfiglet
from pyfiglet import figlet_format
import time
from threading import Thread


def clearScreen():
    os.system('cls')


print(pyfiglet.figlet_format("Jacob Horgan Python Presentation"))
tprint("ONLINE", font="block", chr_ignore=True)
tprint("\nSHARES", font="block", chr_ignore=True)

"""
def updateValues():
    updateShares()
    updateCash()
    updateInvest()


def checkUserInput():


def updateScreen():
    printShares()
    printCash()
    printInvest()
    printMenus()
"""


def startUp():
    db.createTable_Customers()
    db.insert_initailDataSet()
    print(menus.startMenu)
    print(menus.startMenuSwitch(input("Please enter your menu selection: ")))
    if menus.loginMenuActive:
        menus.loginScreen()
    elif menus.registerMenuActive:
        menus.registerScreen()


def updateScreenAccountInfo():

    shares.calculateTotalInvestAccount()

    print("Share Prices:")
    print("Share 1 price per share: ".ljust(
        25, ' '), "£", shares.share1rounded)
    print("Share 2 price per share: ".ljust(
        25, ' '), "£", shares.share2rounded)
    print("Share 3 price per share: ".ljust(
        25, ' '), "£", shares.share3rounded)
    print("\nYour Assets:")
    print("Cash Account Value: ".ljust(25, ' '), "£",
          format(cashAccount.cashAccount, ".2f"))
    print("Investing Account Value: ".ljust(25, ' '), "£",
          format(shares.investAccount, ".2f"))
    print("\n")


def menuLoop():
    if menus.mainMenuActive:
        print(menus.menuPicture)
        updateScreenAccountInfo()
        print(menus.mainMenuSwitch(input("Please enter your menu selection: ")))
    elif menus.depositMenuActive:
        updateScreenAccountInfo()
        print(menus.depositMenuSwitch(
            input("Please enter your menu selection: ")))
    elif menus.withdrawMenuActive:
        updateScreenAccountInfo()
        print(menus.withdrawMenuSwitch(
            input("Please enter your menu selection: ")))
    elif menus.investMenuActive:
        updateScreenAccountInfo()
        print(menus.investMenuSwitch(
            input("Please enter your menu selection: ")))
    elif menus.sharesMenuActive:
        updateScreenAccountInfo()
        print(menus.sharesMenuSwitch(
            input("Please enter your menu selection: ")))
    elif menus.subMenuActive:
        updateScreenAccountInfo()
        print(menus.subMenuSwitch(input("Please enter your menu selection: ")))


def main():
    menuLoop()
    shares.updateAllShares()


startUp()
while 1:
    main()
