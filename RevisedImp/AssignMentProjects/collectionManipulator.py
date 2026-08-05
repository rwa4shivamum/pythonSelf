# Collection Manipulator 

students_list = []

print("==========================================")
print(" Welcome to the Student Data Organizer! ")
print("==========================================")
print("This program allows you to manage student records using Python collections.\n")

running = True

while running:
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")
    
    choice = input("Enter your choice: ").strip()

    if choice == '1':
        print("\nEnter student details:")
        
        student_id = int(input("Student ID: "))
        name = input("Name: ").strip()
        age = int(input("Age: "))
        grade = input("Grade: ").strip()
        dob = input("Date of Birth (YYYY-MM-DD): ").strip()
        
        subjects_input = input("Subjects (comma-separated): ")
        
        subjects_list = []
        for sub in subjects_input.split(','):
            subjects_list.append(sub.strip())

        identity_tuple = (student_id, dob)

        student_dict = {
            "identity": identity_tuple,
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": subjects_list
        }
        students_list.append(student_dict)
        print("\nStudent added successfully!")

    elif choice == '2':
    
        print("\n--- Display All Students ---")
        if len(students_list) == 0:
            print("No student records found.")
        else:
            for student in students_list:
                s_id = student["identity"][0]
                subjects_str = ", ".join(student["subjects"])
                
                print(f"Student ID: {s_id} | Name: {student['name']} | Age: {student['age']} | Grade: {student['grade']} | Subjects: {subjects_str}")

    elif choice == '3':
        print("\n--- Update Student Information ---")
        search_id = int(input("Enter Student ID to update: "))
        found = False

        for student in students_list:
            if student["identity"][0] == search_id:
                found = True
                print(f"Updating record for {student['name']}...")
                
                new_age_input = input("Enter new age (leave blank to keep current): ").strip()
                if new_age_input != "":
                    student["age"] = int(new_age_input)

                new_grade = input("Enter new grade (leave blank to keep current): ").strip()
                if new_grade != "":
                    student["grade"] = new_grade

                new_sub_input = input("Enter new subjects (comma-separated, leave blank to keep current): ").strip()
                if new_sub_input != "":
                    updated_subs = []
                    for sub in new_sub_input.split(','):
                        updated_subs.append(sub.strip())
                    student["subjects"] = updated_subs

                print("Updated Student Record: ID {}, Name {}, Age {}, Grade {}".format(
                    student["identity"][0], student["name"], student["age"], student["grade"]
                ))
                break
        
        if not found:
            print("Student ID not found!")

    elif choice == '4':
        print("\n--- Delete Student ---")
        search_id = int(input("Enter Student ID to delete: "))
        found = False

        for i in range(len(students_list)):
            if students_list[i]["identity"][0] == search_id:
                del students_list[i]
                found = True
                print(f"Student ID {search_id} has been deleted successfully.")
                break
        
        if not found:
            print("Student ID not found!")

    elif choice == '5':
        print("\n--- Display Subjects Offered ---")
    
        all_subjects_set = set()
        for student in students_list:
            for subject in student["subjects"]:
                all_subjects_set.add(subject)

        if len(all_subjects_set) > 0:
            print("Unique Subjects Offered: %s" % ", ".join(all_subjects_set))
        else:
            print("No subjects recorded yet.")

    elif choice == '6':
    
        print("\nThank you for using the Student Data Organizer. Goodbye!")
        running = False

    else:
        print("Invalid option! Please enter a number from 1 to 6.")