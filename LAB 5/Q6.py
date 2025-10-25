def write_questions():
    try:
        sentence = input("Enter a sentence: ")
        if sentence.strip().endswith("?"):
            with open("questions.txt", "a") as f:
                f.write(sentence + "\n")
            print("Question saved to questions.txt")
        else:
            print("Not a question. Nothing saved.")
    except Exception as e:
        print("Unexpected Error:", e)


write_questions()
