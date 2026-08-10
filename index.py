
# ========================================
# STUDENT COURSE & PERFORMANCE MANAGEMENT SYSTEM
# ========================================

students = [
    {
        "id": 101,
        "name": "Raj",
        "age": 20,
        "courses": ["Python", "Java"],
        "skills": {"Python", "SQL", "HTML"},
        "marks": (85, 90, 78)
    }
]


# ========================================
# MAIN MENU
# ========================================

while True:

    print("\n========================================")
    print("STUDENT MANAGEMENT SYSTEM")
    print("========================================")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Student Performance")
    print("7. Course & Skill Analysis")
    print("8. Exit")

    choice = input("Enter your choice: ")


    # ========================================
    # 1. ADD STUDENT
    # ========================================

    if choice == "1":

        print("\n---------- ADD STUDENT ----------")

        student_id = int(input("Enter Student ID: "))

        # Check whether ID already exists
        exists = False

        for student in students:
            if student["id"] == student_id:
                exists = True
                break

        if exists:
            print("Student ID already exists!")

        else:

            name = input("Enter Student Name: ")
            age = int(input("Enter Student Age: "))

            # Courses -> LIST
            course_input = input(
                "Enter courses separated by comma: "
            )

            courses = []

            for course in course_input.split(","):
                courses.append(course.strip())


            # Skills -> SET
            skill_input = input(
                "Enter skills separated by comma: "
            )

            skills = set()

            for skill in skill_input.split(","):
                skills.add(skill.strip())


            # Marks -> TUPLE
            mark1 = int(input("Enter Subject 1 Mark: "))
            mark2 = int(input("Enter Subject 2 Mark: "))
            mark3 = int(input("Enter Subject 3 Mark: "))

            marks = (mark1, mark2, mark3)


            # Student -> DICTIONARY
            student = {
                "id": student_id,
                "name": name,
                "age": age,
                "courses": courses,
                "skills": skills,
                "marks": marks
            }


            # Add dictionary to students LIST
            students.append(student)

            print("Student added successfully!")


    # ========================================
    # 2. VIEW ALL STUDENTS
    # ========================================

    elif choice == "2":

        print("\n---------- ALL STUDENTS ----------")

        if len(students) == 0:
            print("No students available.")

        else:

            for student in students:

                print("\nStudent ID :", student["id"])
                print("Name       :", student["name"])
                print("Age        :", student["age"])
                print("Courses    :", student["courses"])
                print("Skills     :", student["skills"])
                print("Marks      :", student["marks"])


    # ========================================
    # 3. SEARCH STUDENT
    # ========================================

    elif choice == "3":

        print("\n---------- SEARCH STUDENT ----------")

        student_id = int(input("Enter Student ID: "))

        found = False

        for student in students:

            if student["id"] == student_id:

                print("\nStudent Found!")

                print("Student ID :", student["id"])
                print("Name       :", student["name"])
                print("Age        :", student["age"])
                print("Courses    :", student["courses"])
                print("Skills     :", student["skills"])
                print("Marks      :", student["marks"])

                found = True
                break

        if found == False:
            print("Student not found.")


    # ========================================
    # 4. UPDATE STUDENT
    # ========================================

    elif choice == "4":

        print("\n---------- UPDATE STUDENT ----------")

        student_id = int(input("Enter Student ID: "))

        found = False

        for student in students:

            if student["id"] == student_id:

                found = True

                print("\n1. Update Name")
                print("2. Update Age")
                print("3. Update Courses")
                print("4. Update Skills")
                print("5. Update Marks")

                update_choice = input(
                    "Enter your choice: "
                )


                # Update Name
                if update_choice == "1":

                    student["name"] = input(
                        "Enter new name: "
                    )

                    print("Name updated successfully.")


                # Update Age
                elif update_choice == "2":

                    student["age"] = int(
                        input("Enter new age: ")
                    )

                    print("Age updated successfully.")


                # Update Courses
                elif update_choice == "3":

                    course_input = input(
                        "Enter new courses separated by comma: "
                    )

                    courses = []

                    for course in course_input.split(","):
                        courses.append(course.strip())

                    student["courses"] = courses

                    print("Courses updated successfully.")


                # Update Skills
                elif update_choice == "4":

                    skill_input = input(
                        "Enter new skills separated by comma: "
                    )

                    skills = set()

                    for skill in skill_input.split(","):
                        skills.add(skill.strip())

                    student["skills"] = skills

                    print("Skills updated successfully.")


                # Update Marks
                elif update_choice == "5":

                    mark1 = int(
                        input("Enter Subject 1 Mark: ")
                    )

                    mark2 = int(
                        input("Enter Subject 2 Mark: ")
                    )

                    mark3 = int(
                        input("Enter Subject 3 Mark: ")
                    )

                    student["marks"] = (
                        mark1,
                        mark2,
                        mark3
                    )

                    print("Marks updated successfully.")


                else:
                    print("Invalid update choice.")

                break


        if found == False:
            print("Student not found.")


    # ========================================
    # 5. DELETE STUDENT
    # ========================================

    elif choice == "5":

        print("\n---------- DELETE STUDENT ----------")

        student_id = int(input("Enter Student ID: "))

        found = False

        for student in students:

            if student["id"] == student_id:

                students.remove(student)

                found = True

                print("Student deleted successfully.")

                break

        if found == False:
            print("Student not found.")


    # ========================================
    # 6. STUDENT PERFORMANCE
    # ========================================

    elif choice == "6":

        print("\n---------- STUDENT PERFORMANCE ----------")

        student_id = int(input("Enter Student ID: "))

        found = False

        for student in students:

            if student["id"] == student_id:

                found = True

                marks = student["marks"]


                # Total
                total = sum(marks)


                # Average
                average = total / len(marks)


                # Highest
                highest = max(marks)


                # Lowest
                lowest = min(marks)


                print("\nStudent Name :", student["name"])
                print("Marks        :", marks)
                print("Total Marks  :", total)
                print("Average      :", average)
                print("Highest Mark :", highest)
                print("Lowest Mark  :", lowest)


                # Pass / Fail
                if marks[0] >= 40 and marks[1] >= 40 and marks[2] >= 40:
                    print("Result       : PASS")

                else:
                    print("Result       : FAIL")

                break


        if found == False:
            print("Student not found.")


    # ========================================
    # 7. COURSE & SKILL ANALYSIS
    # ========================================

    elif choice == "7":

        print("\n---------- COURSE & SKILL ANALYSIS ----------")


        # ----------------------------------------
        # ALL AVAILABLE COURSES
        # ----------------------------------------

        all_courses = set()

        for student in students:

            for course in student["courses"]:

                all_courses.add(course)


        print("\nAll Available Courses:")

        for course in all_courses:
            print("-", course)


        # ----------------------------------------
        # ALL UNIQUE SKILLS
        # ----------------------------------------

        all_skills = set()

        for student in students:

            for skill in student["skills"]:

                all_skills.add(skill)


        print("\nAll Unique Skills:")

        for skill in all_skills:
            print("-", skill)


        # ----------------------------------------
        # STUDENTS WHO KNOW PYTHON
        # ----------------------------------------

        print("\nStudents who know Python:")

        found_python = False

        for student in students:

            if "Python" in student["skills"]:

                print("-", student["name"])

                found_python = True


        if found_python == False:
            print("No students know Python.")


        # ----------------------------------------
        # COMMON SKILLS BETWEEN TWO STUDENTS
        # ----------------------------------------

        print("\nFind Common Skills Between Two Students")

        id1 = int(input("Enter first Student ID: "))
        id2 = int(input("Enter second Student ID: "))

        student1 = None
        student2 = None


        for student in students:

            if student["id"] == id1:
                student1 = student

            if student["id"] == id2:
                student2 = student


        if student1 is None or student2 is None:

            print("One or both students not found.")

        else:

            common_skills = (
                student1["skills"]
                & student2["skills"]
            )

            print(
                "Common Skills:",
                common_skills
            )


        # ----------------------------------------
        # COUNT STUDENTS IN EACH COURSE
        # ----------------------------------------

        print("\nStudents enrolled in each course:")

        course_count = {}


        for student in students:

            for course in student["courses"]:

                if course in course_count:

                    course_count[course] += 1

                else:

                    course_count[course] = 1


        for course in course_count:

            print(
                course,
                ":",
                course_count[course],
                "student(s)"
            )


    # ========================================
    # 8. EXIT
    # ========================================

    elif choice == "8":

        print("\nThank you for using Student Management System!")

        break


    # ========================================
    # INVALID CHOICE
    # ========================================

    else:

        print("Invalid choice. Please enter 1-8.")

