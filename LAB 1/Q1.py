userInput = input("Enter a number: ")

userInput_float = float(userInput)
userInput_string = str(userInput)
userInput_complex = complex(userInput)
userInput_int = int(float(userInput))   
print("UserInput:", type(userInput))       
print("Float:", type(userInput_float))
print("String:", type(userInput_string))
print("Complex:", type(userInput_complex))

if userInput_int - (userInput_int // 2) * 2 == 0:
    print(f"{userInput_int} is divisible by 2")
else:
    print(f"{userInput_int} is NOT divisible by 2")
