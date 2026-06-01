# Import numpy
import numpy as np

# Create 3D array
arr = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print("3D Array:")
print(arr)

# Iterate using for loop
print("\nUsing For Loop:")

for block in arr:
    for row in block:
        for element in row:
            print(element)

# Iterate using nditer
print("\nUsing nditer:")

for element in np.nditer(arr):
    print(element)