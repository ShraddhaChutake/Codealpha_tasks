#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Students grade tracker
def calculate_average(grades):
    total = sum(grades)
    average = total / len(grades)
    return average

def add_grades(student_grades, student_name, subjects):
    grades = {}
    for subject in subjects:
        grade = float(input(f"Enter {subject} grade for {student_name}: "))
        grades[subject] = grade
    student_grades[student_name] = grades

def display_grades(student_grades, student_name):
    if student_name in student_grades:
        grades = student_grades[student_name]
        print(f"\nGrades for {student_name}:")
        for subject, grade in grades.items():
            print(f"{subject}: {grade}")
        average_grade = calculate_average(grades.values())
        print(f"Average grade: {average_grade:.2f}")
    else:
        print(f"Student '{student_name}' not found.")

def main():
    subjects = ['Math', 'Science', 'English', 'History']  # List of subjects
    student_grades = {}

    while True:
        print("\nOptions:")
        print("1. Add grades for a student")
        print("2. Display grades for a student")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            student_name = input("Enter student's name: ")
            add_grades(student_grades, student_name, subjects)
        elif choice == '2':
            student_name = input("Enter student's name: ")
            display_grades(student_grades, student_name)
        elif choice == '3':
            print("Execution halted.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

