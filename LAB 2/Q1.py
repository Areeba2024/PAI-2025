password = input("Enter your password: ")
digitFound = False
letterFound = False
specialChar = False
if len(password) >= 8:
    for x in password:
        if x.isdigit():
            digitFound = True
        elif x.isalpha():
            letterFound = True
        elif x == '@' or x == '#' or x == '$' or x == '%':
            specialChar = True
    if letterFound == True and digitFound == True and specialChar == True :
         print("VALID PASSWORD")
else:
    print("INVALID PASSWORD")
