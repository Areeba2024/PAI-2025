def checkVowel(userinput):
    if userinput.endswith('a') ==  True or userinput.endswith('e') == True or userinput.endswith('i') == True or userinput.endswith('o') == True or userinput.endswith('u') == True:
        print("Its a vowel")
    else:
        print("Its a consonant")

data = input("Enter a string: ")
checkVowel(data)
