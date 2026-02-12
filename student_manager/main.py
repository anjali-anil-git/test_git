from manager import StudentManager

manager = StudentManager()
manager.load_from_file()

while True:
<<<<<<< HEAD
    print("\n--- Student Management System ---")
=======
    print("\n--- STUDENT SYSTEM (Conflict Version A) ---")
>>>>>>> conflict-demo
    print("1. Add Student")
    print("2. View Students")
    print("3. Save & Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        roll_no = input("Enter roll number: ")
        manager.add_student(name, roll_no)

    elif choice == "2":
        manager.show_students()

    elif choice == "3":
        manager.save_to_file()
        print("Data saved. Exiting program.")
        break

    else:
        print("Invalid choice. Try again.")
