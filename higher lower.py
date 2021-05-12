# display random number 1-13
# show number
# get user to guess h or l
# another num
# see if player correct or wrong

import random

guessList = ("H", "h", "L", "l")

count = 0
gameTrue = True


def inputFunc():
    guess = input("Please input 'H' for Higher or 'L' for Lower: ")
    return guess


while gameTrue:
    print("Let's play Higher or Lower!")
    while count < 5:
        gamePlaying = True
        if count == 0:
            ranNum = random.randrange(1, 14)
        print("\nThe number is: ", ranNum)
        guess = ""
        guess = inputFunc()
        nextRanNum = random.randrange(1, 14)

        if guess in guessList:
            print("Your guess was: ", guess)
            if guess == "H" or guess == "h" and nextRanNum >= ranNum:
                print("The number is: ", nextRanNum)
                print("It was higher, you got it correct! Let's go again.")
                count += 1
            elif guess == "H" or guess == "h" and nextRanNum < ranNum:
                print("The number is: ", nextRanNum)
                print("You got it wrong.")
                print("here")
                gameTrue = False
                gamePlaying = False

            elif guess == "L" or guess == "l" and nextRanNum < ranNum:
                print("The number is: ", nextRanNum)
                print("It was lower, you got it correct! Let's go again.")
                count += 1
            elif guess == "L" or guess == "l" and nextRanNum >= ranNum:
                print("The number is: ", nextRanNum)
                print("You got it wrong.")
                gameTrue = False
                gamePlaying = False

        else:
            print("Please enter a valid input")

        if gamePlaying == False:
            break
        else:
            ranNum = nextRanNum

print("Game Over. your score was: ", count)
