import getpass
#password = getpass.getpass("Enter your password")

first_name = input("Enter your first name: ")
second_name = input("Enter your second name: ")
password = input("Enter a password: ")

full_name = first_name + second_name

print("Your username is " + full_name)

print("Now log on")
username = input("Enter your username: ")
if username == full_name:
    if input("Enter your password: ") == password:
        print("Welcome to your account")
    else:
        print("Your password is incorrect! Please try again.")
else:
    print("Your username is incorrect! Please try again.")
