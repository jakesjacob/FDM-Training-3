techOps = (
    ("Grace", "Zechariah", "Purple"),
    ("Owen",  "Thomas", "Green"),
    ("Sarah", "Jones", "Orange"),
    ("Phil", "Saunders", "Blue"),
    ("Jacob", "Horgan", "Blue"),
    ("Jack", "Mather", "Orange"),
    ("Alisha", "Malster", "Blue"),
    ("Giulia Pia", "Carleton", "Teal"),
    ("Aithsham", "Shah", "Cyan"),
    ("Keh", "Ola", "Green")
)


classNum = len(techOps)


count = 0
count2 = 0


def tupleCheck():
    print("\nThe class favourite colours are:")
    for count in range(0, classNum):
        print(techOps[count][2], end=": ")

    userInput = input(
        "\nEnter someones first name to find out their favourite colour: ")
    for count2 in range(0, classNum):
        if userInput.title() == techOps[count2][0]:
            print("This is " + userInput.title() +
                  " favourite colour: ", techOps[count2][2])


while 1:
    tupleCheck()
