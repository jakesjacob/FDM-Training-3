import menus
import os
from art import *
import pyfiglet
from pyfiglet import figlet_format


def clearScreen():
    os.system('cls')


def mainMenuSwitch(selection):
    # global menus.subMenuActive
    if selection in menus.menuList:
        if selection == "1":
            menus.subMenuActive = True
            clearScreen()
            return menus.menuItem1
        elif selection == "2":
            menus.subMenuActive = True
            clearScreen()
            return menus.menuItem2
        elif selection == "3":
            menus.subMenuActive = True
            clearScreen()
            return menus.menuItem3
        elif selection == "4":
            menus.subMenuActive = True
            clearScreen()
            return menus.menuItem4
        elif selection == "5":
            menus.subMenuActive = True
            clearScreen()
            return menus.menuItem5
    else:
        return "Please enter a valid input"


def subMenuSwitch(selection):
    # global menus.subMenuActive
    if selection in menus.menuList:
        if selection == "1":
            clearScreen()
            return "Item coming soon"
        elif selection == "2":
            clearScreen()
            return "Item coming soon"
        elif selection == "3":
            clearScreen()
            return "Item coming soon"
        elif selection == "4":
            clearScreen()
            return "Item coming soon"
        elif selection == "5":
            clearScreen()
            menus.subMenuActive = False
            return ""
    else:
        return "Please enter a valid input"


print(pyfiglet.figlet_format("Jacob Horgan Python Presentation"))
tprint("ONLINE", font="block", chr_ignore=True)
tprint("\nSHARES", font="block", chr_ignore=True)

while menus.menuActive:
    print(menus.menuPicture)
    print(mainMenuSwitch(input("Please enter your menu selection: ")))
    while menus.subMenuActive:
        print(subMenuSwitch(input("Please enter your menu selection: ")))
