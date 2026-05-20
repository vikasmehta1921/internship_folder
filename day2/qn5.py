# Question 5: Student Marks, Percentage, and Grading System
# In your last program where you find the total and percentage of a student's marks of 5 subject,
# find the grade of the student using conditional statement.
# Grade 'A' if percentage is greater than or equals to 60.
# 'B' for percentage is greater than or equals to 50 and less than 60.
# 'C' for percentage is greater than or equals to 40 and less than 50.
# 'D' for percentage is greater than or equals to 33 and less than 40.
# otherwise 'Fail'

def main():
    print("=== Student Grade Evaluation System ===")
    
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
    
    # Determine the grade using conditional statements
    if percentage >= 60.0:
        grade = "A"
    elif percentage >= 50.0:
        grade = "B"
    elif percentage >= 40.0:
        grade = "C"
    elif percentage >= 33.0:
        grade = "D"
    else:
        grade = "Fail"
    
    # Displaying the formatted result
    print("\n" + "="*40)
    print("            STUDENT REPORT CARD            ")
    print("="*40)
    print(f"Name       : {name}")
    print(f"Class      : {student_class}")
    print(f"Total Marks: {total_marks:.2f} / {max_possible_marks}")
    print(f"Percentage : {percentage:.2f}%")
    print(f"Grade      : {grade}")
    print("="*40)

if __name__ == "__main__":
    main()