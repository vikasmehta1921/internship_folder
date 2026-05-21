name = input("Enter student name: ")
student_class = input("Enter class: ")

mark1 = float(input("Enter marks of Subject 1: "))
mark2 = float(input("Enter marks of Subject 2: "))
mark3 = float(input("Enter marks of Subject 3: "))
mark4 = float(input("Enter marks of Subject 4: "))
mark5 = float(input("Enter marks of Subject 5: "))

total = mark1 + mark2 + mark3 + mark4 + mark5
percentage = (total / 500) * 100

if percentage >= 60:
    grade = "A"
elif percentage >= 50:
    grade = "B"
elif percentage >= 40:
    grade = "C"
elif percentage >= 33:
    grade = "D"
else:
    grade = "Fail"

print("\n----- Student Result -----")
print("Student Name :", name)
print("Class        :", student_class)
print("Total Marks  :", total)
print("Percentage   :", percentage, "%")
print("Grade        :", grade)