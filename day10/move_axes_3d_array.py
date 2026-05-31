# Import numpy
import numpy as np

# Create 3D array
arr = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print("Original 3D Array:")
print(arr)

print("\nShape of Original Array:")
print(arr.shape)

# Move axes to new positions
# axis 0 -> 2
# axis 1 -> 0
# axis 2 -> 1

new_arr = np.moveaxis(arr, [0, 1, 2], [2, 0, 1])

print("\nArray after Moving Axes:")
print(new_arr)

print("\nShape after Moving Axes:")
print(new_arr.shape)