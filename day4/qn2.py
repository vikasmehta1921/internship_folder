def distinct_list(lst):
    new_list = []

    for item in lst:
        if item not in new_list:
            new_list.append(item)

    return new_list

numbers = [1, 2, 3, 2, 4, 1, 5, 3]

print("Original List:", numbers)
print("Distinct List:", distinct_list(numbers))