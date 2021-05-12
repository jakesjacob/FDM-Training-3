import menus
import shares
import cashAccount


import os
from art import *
import pyfiglet
from pyfiglet import figlet_format


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


while 1:
    shares.updateAllShares()
    print(shares.share1)
    print("Cash Account Value: ", cashAccount.cashAccount)
    print(menus.menuPicture)
    print(menus.mainMenuSwitch(input("Please enter your menu selection: ")))

    if menus.depositMenuActive:
        print(menus.depositMenuSwitch(
            input("Please enter your menu selection: ")))
    elif menus.subMenuActive:
        print(menus.subMenuSwitch(input("Please enter your menu selection: ")))
