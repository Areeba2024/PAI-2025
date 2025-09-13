def palindrome(string):
    length = len(string)
    string = string.lower()
    for i in range(length // 2):
        if string[i] != string[length - 1 - i]:
            return False
    return True

word = "maham"
if palindrome(word):
    print("It's a palindrome")
else:
    print("It's not a palindrome")
