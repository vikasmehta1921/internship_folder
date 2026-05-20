# Question 1: Student Marks and Percentage Calculation
# Write a python program that takes in a student name, class.
# It should also take in five subject marks of the students and find the total mark and percentage.
# Display a result in such a way that their name, class, and percentage are printed.

def main():
    print("=== Student Performance Evaluation ===")
    
    # Taking student details
    name = input("Enter Student Name: ").strip()
    student_class = input("Enter Class/Grade: ").strip()
    
    # Taking five subject marks
    print("\nPlease enter marks obtained out of 100 for five subjects:")
    try:
        subject1 = float(input("Subject 1 Mark: "))
        subject2 = float(input("Subject 2 Mark: "))
        subject3 = float(input("Subject 3 Mark: "))
        subject4 = float(input("Subject 4 Mark: "))
        subject5 = float(input("Subject 5 Mark: "))
    except ValueError:
        print("\n[Error] Invalid input! Marks must be numeric values.")
        return

    # Finding total and percentage
    total_marks = subject1 + subject2 + subject3 + subject4 + subject5
    max_possible_marks = 500.0
    percentage = (total_marks / max_possible_marks) * 100
    
    # Displaying the formatted result
    print("\n" + "="*40)
    print("            STUDENT RESULT            ")
    print("="*40)
    print(f"Name       : {name}")
    print(f"Class      : {student_class}")
    print(f"Percentage : {percentage:.2f}%")
    print("="*40)

if __name__ == "__main__":
    main()
