#Automatic dice roller
#Ben Lepsch 8-23-2018

from random import randint

print("Automatic Dice Roller")
print(randint(1,6))

while True:
    userInput = input("Press x to exit and press enter to roll again.   ")
    if userInput == "":
        value = randint(1,6)
        print(value)

    if userInput == "x":
        break
