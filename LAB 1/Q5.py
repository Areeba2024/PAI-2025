name = input("Enter your name: ")
year = input("Enter your birth year: ")
part1 = name[:3].title()
part2 = year[-2:]
symbols = "@#%&*"
ascii_value = ord(name[0].lower())
part3 = symbols[ascii_value % len(symbols)]
password = part1 + part2 + part3
print("Generated Password:", password)