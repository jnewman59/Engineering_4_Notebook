sentence = input("Type a simple sentence: ")
wordList = sentence.split(' ')
for word in wordList:
    for char in word:
        print(char)
    print('-')
