# Student Result with Grade

name = input("Enter student name: ")
student_class = input("Enter class: ")

sub1 = int(input("Enter Subject 1 marks: "))
sub2 = int(input("Enter Subject 2 marks: "))
sub3 = int(input("Enter Subject 3 marks: "))
sub4 = int(input("Enter Subject 4 marks: "))
sub5 = int(input("Enter Subject 5 marks: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total / 5

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

print("\n-----Result-----")
print("Name:", name)
print("Class:", student_class)
print("Total:", total)
print("Percentage:", percentage)
print("Grade:", grade)