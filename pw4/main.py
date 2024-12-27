from domains.student import student
from domains.course import course
from input import add_student, add_course, input_marks, cal_gpa
from output import list_students, list_courses, show_marks
students = []
courses = []
marks = {}
def main():
        while True:
            print("\n1. Add students")
            print("2. Add courses")
            print("3. Input marks for a course")
            print("4. Calculate GPA")
            print("5. List students")
            print("6. List courses")
            print("7. Show marks for a course")
            print("8. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                add_student(students)
            elif choice == "2":
                add_course(courses)
            elif choice == "3":
                input_marks(courses, marks, students)
            elif choice == "4":
                cal_gpa(students)
            elif choice == "5":
                list_students(students)
            elif choice == "6":
                list_courses(courses)
            elif choice == "7":
                show_marks(marks, students)
            elif choice == "8":
                print("Exiting program...")
                break
            else:
                print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()