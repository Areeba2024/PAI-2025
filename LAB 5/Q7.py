def fix_mistake():
    try:
        with open("replacement_needed.txt", "r") as f:
            content = f.read()

        print("Original content:", content)

        old = input("Enter the wrong letter to replace: ")
        new = input("Enter the correct letter: ")

        if old in content:
            content = content.replace(old, new)
            with open("replacement_needed.txt", "w") as f:
                f.write(content)
            print("File updated successfully.")
        else:
            print("No such letter found in the file.")

    except FileNotFoundError:
        print("Error: replacement_needed.txt not found.")
    except Exception as e:
        print("Unexpected Error:", e)


fix_mistake()
