import os
import cashAccount
import shares
import time


mainMenuList = ("1", "2", "3", "4", "5", "X", "x")
sharesMenuList = ("1", "2", "3", "X", "x")
cashMenuList = ("1", "X", "x")

mainMenuActive = True
subMenuActive = False
depositMenuActive = False
withdrawMenuActive = False
investMenuActive = False
sharesMenuActive = False


def clearScreen():
    os.system('cls')


def updateScreenAccountInfo():
    print(shares.share1)
    print(shares.share2)
    print(shares.share3)
    print("Cash Account Value: ", cashAccount.cashAccount)


def mainMenuSwitch(selection):
    global mainMenuActive
    global subMenuActive
    global depositMenuActive
    global withdrawMenuActive
    global sharesMenuActive
    if selection in mainMenuList:
        if selection == "1":
            depositMenuActive = True
            mainMenuActive = False
            clearScreen()
            return menuItem1
        elif selection == "2":
            withdrawMenuActive = True
            mainMenuActive = False
            clearScreen()
            return menuItem2
        elif selection == "3":
            subMenuActive = True
            mainMenuActive = False
            clearScreen()
            return menuItem3
        elif selection == "4":
            sharesMenuActive = True
            mainMenuActive = False
            clearScreen()
            return print(menuItem4.format(shares.share1, shares.share2, shares.share3))
        elif selection == "5":
            subMenuActive = True
            mainMenuActive = False
            clearScreen()
            return menuItem5
    else:
        print("Please enter a valid input")
        mainMenuSwitch(input("Please enter your menu selection: "))


def subMenuSwitch(selection):
    global mainMenuActive
    global subMenuActive
    if selection in mainMenuList:
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
        elif selection == "X" or selection == "x":
            clearScreen()
            subMenuActive = False
            mainMenuActive = True
            return ""
    else:
        print("Please enter a valid input")
        subMenuSwitch(input("Please enter your menu selection: "))


def depositMenuSwitch(selection):
    global mainMenuActive
    global depositMenuActive
    if selection in cashMenuList:
        if selection == "1":
            cashAccount.depositScreen()
            time.sleep(2)
            clearScreen()
            depositMenuActive = False
            mainMenuActive = True
        elif selection == "X" or selection == "x":
            clearScreen()
            depositMenuActive = False
            mainMenuActive = True
            return ""
    else:
        print("Please enter a valid input")
        depositMenuSwitch(input("Please enter your menu selection: "))


def withdrawMenuSwitch(selection):
    global mainMenuActive
    global withdrawMenuActive
    if selection in cashMenuList:
        if selection == "1":
            cashAccount.withdrawScreen()
            time.sleep(2)
            clearScreen()
            withdrawMenuActive = False
            mainMenuActive = True
        elif selection == "X" or selection == "x":
            clearScreen()
            withdrawMenuActive = False
            mainMenuActive = True
            return ""
    else:
        print("Please enter a valid input")
        withdrawMenuSwitch(input("Please enter your menu selection: "))


def sharesMenuSwitch(selection):
    global mainMenuActive
    global sharesMenuActive
    if selection in sharesMenuList:
        if selection == "1":
            clearScreen()
            mainMenuActive = True
            sharesMenuActive = False
        elif selection == "2":
            clearScreen()
            mainMenuActive = True
            sharesMenuActive = False
        elif selection == "3":
            clearScreen()
            mainMenuActive = True
            sharesMenuActive = False
        elif selection == "X" or selection == "x":
            clearScreen()
            sharesMenuActive = False
            mainMenuActive = True
            return ""
    else:
        print("Please enter a valid input")
        sharesMenuSwitch(input("Please enter your menu selection: "))


menuPicture = """

                                        #############################################
                                        #               MAIN MENU                   #
                                        #                                           #
                                        #       1 -     Cash Deposit                #
                                        #       2 -     Cash Withdraw               #
                                        #       3 -     Invest Account              #
                                        #       4 -     Shares Info                 #
                                        #       5 -     Account Info                #
                                        #                                           #
                                        #############################################

"""

menuItem1 = """


                                        #############################################
                                        #               CASH DEPOSIT                #             
                                        #                                           #
                                        #       Deposits will be rounded to         #
                                        #       the nearest £. Limit of £500.       #
                                        #                                           #
                                        #       1 -     Proceed                     #
                                        #       X -     Back to Main Menu           #
                                        #                                           #
                                        #############################################

"""

menuItem2 = """


                                        #############################################
                                        #               CASH WITHDRAW               #             
                                        #                                           #
                                        #       No limit, but you can't             #
                                        #       withdraw money you don't have.      #
                                        #                                           #
                                        #       1 -     Proceed                     #
                                        #       X -     Back to Main Menu           #
                                        #                                           #
                                        #############################################

"""

menuItem3 = """


                                        #############################################
                                        #               INVEST ACCOUNT              #             
                                        #                                           #
                                        #       1 -                                 #
                                        #       2 -                                 #
                                        #       3 -                                 #
                                        #       4 -                                 #
                                        #       X -     Back to Main Menu           #
                                        #                                           #
                                        #############################################

"""

menuItem4 = """


                                        #############################################
                                        #               SHARES INFO                 #             
                                        #                                           #
                                        #       1 -     Share 1 = {0:.2f}              #
                                        #       2 -     Share 2 = {1:.2f}              #
                                        #       3 -     Share 3 = {2:.2f}              #
                                        #                                           #
                                        #       X -     Back to Main Menu           #
                                        #                                           #
                                        #############################################

"""

menuItem5 = """


                                        #############################################
                                        #               ACCOUNT INFO                #             
                                        #                                           #
                                        #       1 -                                 #
                                        #       2 -                                 #
                                        #       3 -                                 #
                                        #       4 -                                 #
                                        #       X -     Back to Main Menu           #
                                        #                                           #
                                        #############################################

"""
