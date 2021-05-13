from art import *
import pyfiglet
from pyfiglet import figlet_format


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
                                        #       1 -                                 #
                                        #       2 -                                 #
                                        #       3 -                                 #
                                        #       4 -                                 #
                                        #       5 -     Back to Main Menu           #
                                        #                                           #
                                        #############################################

"""

menuItem2 = """

                                        #############################################
                                        #               CASH WITHDRAW               #             
                                        #                                           #
                                        #       1 -                                 #
                                        #       2 -                                 #
                                        #       3 -                                 #
                                        #       4 -                                 #
                                        #       5 -     Back to Main Menu           #
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
                                        #       5 -     Back to Main Menu           #
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
                                        #       5 -     Back to Main Menu           #
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
                                        #       5 -     Back to Main Menu           #
                                        #                                           #
                                        #############################################

"""

menuList = ("1", "2", "3", "4", "5")
menuActive = True
subMenuActive = False


def mainMenuSwitch(selection):
    global subMenuActive
    if selection in menuList:
        if selection == "1":
            subMenuActive = True
            return menuItem1
        elif selection == "2":
            subMenuActive = True
            return menuItem2
        elif selection == "3":
            subMenuActive = True
            return menuItem3
        elif selection == "4":
            subMenuActive = True
            return menuItem4
        elif selection == "5":
            subMenuActive = True
            return menuItem5
    else:
        return "Please enter a valid input"


def subMenuSwitch(selection):
    global subMenuActive
    if selection in menuList:
        if selection == "1":
            return "Item coming soon"
        elif selection == "2":
            return "Item coming soon"
        elif selection == "3":
            return "Item coming soon"
        elif selection == "4":
            return "Item coming soon"
        elif selection == "5":
            subMenuActive = False
            return ""
    else:
        return "Please enter a valid input"


#tprint("JACOB", font="block", chr_ignore=True)
#tprint("HORGAN", font="block", chr_ignore=True)

print(pyfiglet.figlet_format("Jacob Horgan Python Presentation"))
tprint("ONLINE", font="block", chr_ignore=True)
tprint("\nSHARES", font="block", chr_ignore=True)
while menuActive:
    print(menuPicture)
    print(mainMenuSwitch(input("Please enter your menu selection: ")))
    while subMenuActive:
        print(subMenuSwitch(input("Please enter your menu selection: ")))
