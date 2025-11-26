# A list to store student data, where each element is a dictionary:
# {"name": <student_name>, "grades": [list_of_grades]}
students= []


def add_student():
    """
    Adds a new student to the system
    Prompts the user for a student name and checks for duplicates.
    """
    student_name = input("Enter student name: ").strip().title()

    # Check if student already exists
    for student in students:
        if student["name"].lower() == student_name.lower():
            print(f"Error: Student {student_name} already exists in the system")
            return

    # Add new student
    students.append({"name" : student_name,
                     "grades" : []})
    print(f"Student {student_name} added successfully")

def check_students():
    """
    Ensures the students list is not empty.
    :return: True if data exists, otherwise prints a warning and returns False
    """
    if not students:
        print("There are no students in the system")
        return False
    return True

def add_grade_for_student():
    """
    Adds grades to a specific student.
    Uses a loop to accept multiple grades until the user enters 'done'.
    Includes error handling for invalid input.
    """
    if not check_students():
        return

    student_name = input("Enter student name: ").strip().title()

    #  Check student name in system
    for student in students:
        if student["name"].lower() == student_name.lower():
            # Input loop for grades
            while True:
                grade_input = input("Enter a grade or 'done' to finish: ").strip().lower()

                if grade_input == 'done':
                    break

                try:
                    grade_val = int(grade_input)
                    if 0 <= grade_val <= 100:
                        student["grades"].append(grade_val)
                    else:
                        print("Error: the grade must be between 1 and 100")
                except ValueError:
                    print("Error: The grade must be integer or 'done'")
            return

    print(f"Student {student_name} not found.")

def show_report():
    """
    Generates a detailed report of all students:
    Displays each student's average grade (N/A if no grades)
    Shows max, min, and overall average across all students with grades
    """
    if not check_students():
        return

    average_grades = []

    print('--- Student report ---')

    for student in students:
        try:
            average = sum(student["grades"]) / len(student["grades"])
            average_grades.append(average)
            print(f"{student['name']}'s average grade is {average:.2f}")
        except ZeroDivisionError:
            print(f"{student['name']}'s average grade is N/A")

    # Check available grades to calculate
    if not average_grades:
        print("No grades available to calculate")
        return

    # Summary statistics
    print('--------------------------------------')
    print(f'Max Average: {max(average_grades):.2f}')
    print(f'Min Average: {min(average_grades):.2f}')
    print(f'Overall Average: {sum(average_grades)/len(average_grades):.2f}')

def find_top_student():
    """
    Finds and prints the student with the highest average grade.
    """
    if not check_students():
        return

    # Find students with grades
    students_with_grades = [student for student in students if student["grades"]]

    if not students_with_grades:
        print("No students with grades")
        return

    # Determine the best student
    best = max(students_with_grades,
               key=lambda student: sum(student["grades"]) / len(student["grades"]))

    best_avg = sum(best["grades"]) / len(best["grades"])

    print(f"The student with the highest average is {best['name']} with a grade of {best_avg}")

def main():
    """
    Main menu loop that navigates the application.
    Uses try/except to handle invalid numeric input from the user.
    """
    while True:
        print("--- Student Grade Analyzer --- \n"
            "1. Add a new student \n"
              "2. Add grades for a student \n"
              "3. Generate a full report \n"
              "4. Find the top student \n"
              "5. Exit program")

        try:
            user_choice = int(input("Enter your choice: "))
            if 1 <= user_choice <= 5:
                if user_choice == 1:
                    add_student()
                elif user_choice == 2:
                    add_grade_for_student()
                elif user_choice == 3:
                    show_report()
                elif user_choice == 4:
                    find_top_student()
                elif user_choice == 5:
                    break
            else:
                print("Error: your input must be between 1 and 5")

        except ValueError:
            print("Error: Your input must be a number")


main()







