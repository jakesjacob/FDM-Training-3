# get full name
# get dob

# return users age
# say users age on next birthday

from datetime import datetime


def getName():
    firstName = input("Please type your first name: ")
    secondName = input("Please type your second name: ")
    firstNameCap = firstName.capitalize()
    secondNameCap = secondName.capitalize()
    fullName = (firstNameCap + " " + secondNameCap)
    print("Hello", fullName)


def getDOB():
    dob = input("\n\nPlease enter your DOB (dd-mm-yyyy)")
    datetimeDate = datetime.strptime(dob, "%d-%m-%Y")
    today = datetime.today()
    difference = today - datetimeDate
    age = int(difference.days/365)
    age1 = age + 1
    print("Your age is: ", age)
    txt = ("You will be {} on your next birthday")
    print(txt.format(age1))


getDOB()
getName()
