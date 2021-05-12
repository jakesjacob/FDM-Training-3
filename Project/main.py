import menus
import shares
import cashAccount


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


def updateScreenAccountInfo():
    print("Share 1 price: ".ljust(25, ' '), shares.share1rounded)
    print("Share 2 price: ".ljust(25, ' '), shares.share2rounded)
    print("Share 2 price: ".ljust(25, ' '), shares.share3rounded)
    print("Cash Account Value: ".ljust(25, ' '), cashAccount.cashAccount)
    print("Investing Account Value: ".ljust(25, ' '), cashAccount.cashAccount)
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
    elif menus.sharesMenuActive:
        updateScreenAccountInfo()
        print(menus.sharesMenuSwitch(
            input("Please enter your menu selection: ")))
    elif menus.subMenuActive:
        updateScreenAccountInfo()
        print(menus.subMenuSwitch(input("Please enter your menu selection: ")))


while 1:
    menuLoop()
    shares.updateAllShares()
