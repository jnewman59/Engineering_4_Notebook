#import subprocess, os

word = input("Select the word: ")
print("\n"*50)

#def cls():
#    cls = os.system("CLS")
#cls()
hangmanCounter = 0
won = False
lettersGuessed = []

def printHangman(n):
    print('---┐')
    hangmanArr = ['   O\n', '   |\n', '  /', '|', '\\\n', '   |\n', '  /', ' \\\n']
    if n != 3:
        hangmanStr = ''
        for i in range(0, n):
            hangmanStr += hangmanArr[i]
        print(hangmanStr)
    else:
        print('   O\n   |\n   |')


while not won and hangmanCounter < 8:
    print('\n\n\n')
    printString = ''
    for char in word:
        printString += (char + ' ') if char in lettersGuessed else '_ '
    print(printString)
    guessLetter = 'oops'
    
    while len(guessLetter)!=1 or not guessLetter.isalpha() or guessLetter in lettersGuessed:
        guessLetter = input("Enter a single letter to guess. " + ("You have already guessed these letters: " + ( (str(lettersGuessed) ) [1:len(str(lettersGuessed) )-1] + '\n') if len(lettersGuessed)>0 else '\n') )
        if len(guessLetter) != 1 or not guessLetter.isalpha():
            print("That is not a letter. Try again.\n")
        if guessLetter in lettersGuessed:
            print("You have already guessed that letter. Try again.\n")

    lettersGuessed.append(guessLetter)
    won = True
    for char in word:
        if not char in lettersGuessed:
            won = False
    if won or hangmanCounter >= 8:
        break
    if guessLetter in word:
        print("Congrats! You guessed one of the word's letters.\n")
    else:
        print("Sorry, that letter is not in the word.\n")
        hangmanCounter += 1
    print("Your hangman status: ")
    printHangman(hangmanCounter)

    

if won:
    print("Congrats! You won! The word was " +word +'.\n')
    print("This is how close you were to being hung:")
else:
    print("Sorry, you have been hung.")
printHangman(hangmanCounter)
            
    
