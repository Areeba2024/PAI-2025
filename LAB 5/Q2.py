def replace_words(data,newData):
    try:
        with open("data.txt","r") as f:
            content = f.read()
            if data in content:
                content = content.replace(data,newData)
            else:
                print("No such word exist")
        with open("data.txt","w") as f:
            f.write(content)
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("Unexpected Error:", e)

dataReplace = input("Enter the data to be replaced: ")
newData = input("Enter the new data: ")
replace_words(dataReplace,newData)