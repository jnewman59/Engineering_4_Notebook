#Ben and Jonah
#Strings and lOOps

sentence = input("Type a simple sentence: \t")

s_list = sentence.split()

for word in s_list:
    for letter in word:
        print(letter)
    print('-')
    
