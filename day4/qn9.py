def count_case_letters(string):
    upper = 0
    lower = 0

    for char in string:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1

    print("Upper case letters:", upper)
    print("Lower case letters:", lower)

text = input("Enter a string: ")

count_case_letters(text)