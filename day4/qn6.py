def check_range(num, start, end):
    if num >= start and num <= end:
        return True
    else:
        return False

number = int(input("Enter number: "))
start_range = int(input("Enter start of range: "))
end_range = int(input("Enter end of range: "))

if check_range(number, start_range, end_range):
    print(number, "falls within the range.")
else:
    print(number, "does not fall within the range.")