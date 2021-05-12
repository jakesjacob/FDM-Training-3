import os
import cashAccount


menuList = ("1", "2", "3", "4", "5", "X", "x")
cashMenuList = ("1", "X", "x")

menuActive = True
subMenuActive = False
depositMenuActive = False


def clearScreen():
    os.system('cls')


def mainMenuSwitch(selection):
    global subMenuActive
    global depositMenuActive
    if selection in menuList:
        if selection == "1":
            depositMenuActive = True
            clearScreen()
            return menuItem1
        elif selection == "2":
            subMenuActive = True
            clearScreen()
            return menuItem2
        elif selection == "3":
            subMenuActive = True
            clearScreen()
            return menuItem3
        elif selection == "4":
            subMenuActive = True
            clearScreen()
            return menuItem4
        elif selection == "5":
            subMenuActive = True
            clearScreen()
            return menuItem5
    else:
        return "Please enter a valid input"


def subMenuSwitch(selection):
    global subMenuActive
    if selection in menuList:
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
            return ""
    else:
        return "Please enter a valid input"


def depositMenuSwitch(selection):
    global depositMenuActive
    if selection in cashMenuList:
        if selection == "1":
            cashAccount.depositScreen()
            depositMenuActive = False
        elif selection == "X" or selection == "x":
            clearScreen()
            depositMenuActive = False
            return ""
    else:
        print("Please enter a valid input")
        depositMenuSwitch(input("Please enter your menu selection: "))


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
                                        #       1 -                                 #
                                        #       2 -                                 #
                                        #       3 -                                 #
                                        #       4 -                                 #
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
