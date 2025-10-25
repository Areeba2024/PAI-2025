
def count_chars_and_words():
    try:
        with open("data.txt", 'r') as f:
            content = f.read()
        char_count = len(content)
        word_count = len(content.split())

        print(f"Total Characters: {char_count}")
        print(f"Total Words: {word_count}")

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("Unexpected Error:", e)

count_chars_and_words()
