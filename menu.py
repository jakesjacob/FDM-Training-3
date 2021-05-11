from art import *

menuPicture = """

#############################################
#                                           #
#       1 -     Menu Item 1                 #
#       2 -     Menu Item 2                 #
#       3 -     Menu Item 3                 #
#       4 -     Menu Item 4                 #
#       5 -     Menu Item 5                 #
#                                           #
#############################################

"""


def menuSwitch(selection):
    if selection == "1":
        return "Menu Item 1"
    elif selection == "2":
        return "Menu Item 2"
    elif selection == "3":
        return "Menu Item 3"
    elif selection == "4":
        return "Menu Item 4"
    elif selection == "5":
        return "Menu Item 5"


menuActive = True

while menuActive:
    print(menuPicture)
    print(menuSwitch(input("Please enter your menu selection: ")))
