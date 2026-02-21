from models import Student, Classroom
import analsyis
import utils

def main():
    my_classroom = Classroom() 
    saved_students = utils.load_student() 
    for s in saved_students:
        my_classroom.add_student(s) 

    while True:
        print("\n--- Student Performance Analyzer ---") 
        print("1. Add Student")
        print("2. Search Student")
        print("3. Remove Student")
        print("4. Student Average")
        print("5. Student Grade Category")
        print("6. Classroom Average")
        print("7. Top Performing Student")
        print("8. Lowest Performing Student")
        print("9. Grade Distribution")
        print("10. Save and Exit")

        choice = input("\nSelect an option (1-10): ") 

        match choice: 
            case "1":
                name = input("Enter Name: ")
                s_id = input("Enter ID: ")
                if utils.Validator.is_valid_name(name) and utils.Validator.is_valid_id(s_id): 
                    try:
                        grades_input = input("Enter grades (separated by comma, e.g., 85,90,70): ")
                        grades = [float(g.strip()) for g in grades_input.split(",")] 
                        
                        if all(utils.Validator.is_valid_grade(g) for g in grades): 
                            new_student = Student(name, s_id, grades) 
                            my_classroom.add_student(new_student) 
                            print("Student added successfully!")
                        else:
                            print("Error: One or more grades are invalid (must be 0-100).") 
                    except ValueError:
                        print("Error: Please enter numeric grades only.") 
                else:
                    print("Error: Invalid Name or ID format.") 

            case "2":
                s_id = input("Enter Student ID to search: ")
                student = my_classroom.search_student(s_id) 
                if student:
                    print(f"Found: {student.name}, ID: {student.student_id}, Grades: {student.grades}")
                else:
                    print("Student not found.")

            case "3":
                s_id = input("Enter Student ID to remove: ")
                if my_classroom.remove_student(s_id): 
                    print("Student removed successfully.")
                else:
                    print("Student not found.")

            case "4":
                s_id = input("Enter Student ID to see average: ")
                student = my_classroom.search_student(s_id) 
                if student:
                    print(f"{student.name}'s Average: {student.calculate_average():.2f}") 
                else:
                    print("Student not found.")

            case "5":
                s_id = input("Enter Student ID to see category: ")
                student = my_classroom.search_student(s_id) 
                if student:
                    print(f"{student.name}'s Category: {student.grade_category()}") 
                else:
                    print("Student not found.")

            case "6":
                avg = my_classroom.calculate_classroom_average() 
                print(f"Classroom Overall Average: {avg:.2f}")

            case "7":
                top = analsyis.get_top_student(my_classroom) 
                if top:
                    print(f"Top Student: {top.name} with Average: {top.calculate_average():.2f}")
                else:
                    print("No data available.")

            case "8":
                low = analsyis.get_lowest_student(my_classroom) 
                if low:
                    print(f"Lowest Student: {low.name} with Average: {low.calculate_average():.2f}")
                else:
                    print("No data available.")

            case "9":
                dist = analsyis.grade_distribution(my_classroom) 
                print("Grade Distribution:")
                for category, count in dist.items():
                    print(f"- {category}: {count}")

            case "10":
                utils.save_to_csv(my_classroom) 
                print("Data saved successfully. Exiting...")
                break

            case _:
                print("Invalid choice, please select between 1-10.") 

if __name__ == "__main__":
    main()