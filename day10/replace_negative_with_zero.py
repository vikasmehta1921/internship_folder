# Import numpy
import numpy as np

# Create array
arr = np.array([10, -5, 20, -8, 30, -2])

print("Original Array:")
print(arr)

# Replace negative values with 0
arr[arr < 0] = 0

print("\nArray after replacing negative values with 0:")
print(arr)