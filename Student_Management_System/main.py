students = []

while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Student Name: ")
        roll_no = input("Enter Roll Number: ")
        department = input("Enter Department: ")

        student = {
            "name": name,
            "roll_no": roll_no,
            "department": department
        }

        students.append(student)
        print("✅ Student Added Successfully")

    elif choice == "2":

        if len(students) == 0:
            print("No students found")

        else:
            print("\nSaved Students:")

            for student in students:
                print(
                    f"Name: {student['name']}, "
                    f"Roll No: {student['roll_no']}, "
                    f"Department: {student['department']}"
                )

    elif choice == "3":
        search_name = input("Enter student name to search: ")

        found = False

        for student in students:
            if student["name"].lower() == search_name.lower():
                print("Student Found:")
                print(student)
                found = True

        if not found:
            print("❌ Student Not Found")

    elif choice == "4":
        delete_name = input("Enter student name to delete: ")

        found = False

        for student in students:
            if student["name"].lower() == delete_name.lower():
                students.remove(student)
                print("🗑️ Student Deleted Successfully")
                found = True

        if not found:
            print("❌ Student Not Found")

    elif choice == "5":
        print("Exiting Student Management System...")
        break

    else:
        print("❌ Invalid Choice. Please Try Again.")