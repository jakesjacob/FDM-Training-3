"""
Update your program to ask the user to type in their Username and Password.

Check if the Username is one of the following (display appropriate message):

allUserList = ['UK_User1', 'US_User2', 'Africa_User3', 'Canada_User4' , 'Australia_User6']


"""

username = input("Enter your username: ")
password = input("Enter your password: ")

allUserList = ['UK_User1', 'US_User2',
               'Africa_User3', 'Canada_User4', 'Australia_User6']

if username in allUserList:
    print("Username correct.")
else:
    print("Incorrect. try again.")
