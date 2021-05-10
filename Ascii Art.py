# Use ascii to art to print to screen
# create variable
# store name input
# print the variable

#import pyfiglet

from termcolor import cprint
from pyfiglet import figlet_format
from colorama import init
import sys
import pyfiglet
from art import *

#tprint("Jacob", font="rnd-large")
tprint("INVEST", font="block", chr_ignore=True)

ascii_art101 = pyfiglet.figlet_format("Hello Lauren")
print(ascii_art101)

init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected

#cprint(figlet_format('Jacob', font='avatar'), 'blue', 'on_red', attrs=['bold'])

print("Please input your name")
nameVar = input("")

asciiJACOB = """
#####  ###   ####  ###  ####
  #   #   # #     #   # #   #
  #   ##### #     #   # ####
  #   #   # #     #   # #   #
###   #   #  ####  ###  ####
"""

asciiJ = """
#####
  #
  #
  #
###
"""

asciiA = """
 ### 
#   #
#####
#   #
#   #
"""

asciiC = """
 ####
#    
#    
#    
 ####
"""

asciiO = """
 ### 
#   #
#   #
#   #
 ### 
"""

asciiB = """
####
#   #
####
#   #
####
"""

output = ""

for c in nameVar:
    if c == "J":
        # print(asciiJ)
        output = output + asciiJ
    elif c == "A":
        # print(asciiA)
        output = output + asciiA
    elif c == "C":
        # print(asciiC)
        output = output + asciiC
    elif c == "O":
        # print(asciiO)
        output = output + asciiO
    elif c == "B":
        # print(asciiB)
        output = output + asciiB


print(output)


# print(asciiJACOB)

greetings = input()
print(greetings)
print("Hello ", greetings, " !")

first_name = input("Enter your first name: ")
second_name = input("Enter your second name: ")

full_name = first_name + second_name

print("Hello " + full_name)
