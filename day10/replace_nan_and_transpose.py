# Import numpy
import numpy as np

# Create 2D array
arr = np.array([
    [6, -8, 73, -110],
    [np.nan, -8, 0, 94]
])

print("Original Array:")
print(arr)

# Replace NaN with 0
arr = np.nan_to_num(arr, nan=0)

print("\nArray after replacing NaN with 0:")
print(arr)

# Interchange rows and columns using transpose
arr = arr.T

print("\nArray after interchanging rows and columns:")
print(arr)