# Import numpy
import numpy as np

# Create 1D array
arr1 = np.array([1, 2, 3])

# Create 2D array
arr2 = np.array([
    [4, 5, 6],
    [7, 8, 9]
])

print("1D Array:")
print(arr1)

print("\n2D Array:")
print(arr2)

# Combine arrays
combined = np.vstack((arr2, arr1))

print("\nCombined Array:")
print(combined)