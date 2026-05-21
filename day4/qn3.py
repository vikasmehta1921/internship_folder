def multiply_list(lst):
    result = 1

    for num in lst:
        result *= num

    return result

numbers = [2, 3, 4, 5]

print("List:", numbers)
print("Multiplication of all numbers:", multiply_list(numbers))