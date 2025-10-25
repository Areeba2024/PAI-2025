def divide_numbers():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Please enter valid integer numbers.")
    except Exception as e:
        print("Unexpected Error:", e)


divide_numbers()
