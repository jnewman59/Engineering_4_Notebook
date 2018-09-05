import subprocess, os
word = '3'
while not word.isalpha():
    word = input("Select the word: ")
    if not word.isalpha():
        print("That is not a word. Please try again.\n")
print("\n"*50)

cls = os.system("CLS")

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
    if guessLetter in word:
        print("You guessed one of the word's letters!\n")
    else:
        print("Sorry, that letter is not in the word.\n")
        hangmanCounter += 1
    if won or hangmanCounter >= 8:
        break
    print("Your hangman status: ")
    
    printHangman(hangmanCounter)

    

if won:
    print("Congrats! You won! The word was " +word +'.\n')
    print("This is how close you were to being hung:")
else:
    print("You have been hung.")
printHangman(hangmanCounter)
            
    
