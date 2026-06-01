# Import numpy
import numpy as np

# Create array
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Array:")
print(arr)

# Maximum value
print("\nMaximum Value:")
print(np.max(arr))

# Minimum value
print("\nMinimum Value:")
print(np.min(arr))

# Number of rows and columns
rows, cols = arr.shape

print("\nRows:", rows)
print("Columns:", cols)

# Select each element
print("\nEach Element:")

for row in arr:
    for element in row:
        print(element)

# Specific element
print("\nSpecific Element:")
print(arr[1, 2])

# Sum using for loop
sum_value = 0

for row in arr:
    for element in row:
        sum_value += element

print("\nSum of Array:")
print(sum_value)

# Second array
arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Addition
print("\nAddition:")
print(arr + arr2)

# Subtraction
print("\nSubtraction:")
print(arr - arr2)

# Multiplication
print("\nMultiplication:")
print(arr * arr2)

# Division
print("\nDivision:")
print(arr / arr2)