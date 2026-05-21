def print_even_numbers(lst):
    print("Even numbers are:")

    for num in lst:
        if num % 2 == 0:
            print(num)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print_even_numbers(numbers)