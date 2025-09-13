students = {} 

while True:
    print("\nStudent Management System ")
    print("1. Add Student")
    print("2. Update Marks")
    print("3. Delete Student")
    print("4. Find Topper")
    print("5. Show All Students")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print(f"{name} added successfully.")

    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in students:
            marks = int(input("Enter new marks: "))
            students[name] = marks
            print(f"{name}'s marks updated.")
        else:
            print("Student not found!")

    elif choice == "3":
        name = input("Enter student name to delete: ")
        if name in students:
            del students[name]
            print(f"{name} deleted successfully.")
        else:
            print("Student not found!")

    elif choice == "4":
        if students:
            topper = max(students, key=students.get)
            print(f"Topper: {topper} with {students[topper]} marks")
        else:
            print("No students available.")

    elif choice == "5":
        if students:
            print("All Students:")
            for name, marks in students.items():
                print(f"{name} - {marks}")
        else:
            print("No student records yet.")

    elif choice == "6":
        print("Exit")
        break

    else:
        print("Invalid choice. Try again!")
