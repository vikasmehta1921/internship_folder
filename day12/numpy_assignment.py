# Import numpy
import numpy as np

# Create 1D array
arr1 = np.array([10, 20, 30, 40, 50, 60])

print("1D Array:")
print(arr1)

# Convert 1D array to 2D
arr2d = arr1.reshape(2, 3)

print("\n2D Array:")
print(arr2d)

# Print array attributes
print("\nShape:")
print(arr2d.shape)

print("\nDimension:")
print(arr2d.ndim)

print("\nData Type:")
print(arr2d.dtype)

print("\nItem Size:")
print(arr2d.itemsize)

# Create 3x3 array of all 9
arr9 = np.full((3, 3), 9)

print("\n3x3 Array of 9:")
print(arr9)

# Create evenly spaced values
even_values = np.linspace(25, 125, 10)

print("\n10 Evenly Spaced Values:")
print(even_values)

# Convert Python list into NumPy array
my_list = [5, 10, 15, 20]

numpy_array = np.array(my_list)

print("\nConverted NumPy Array:")
print(numpy_array)

# Reverse a 1D array
reverse_array = numpy_array[::-1]

print("\nReversed Array:")
print(reverse_array)

# Create 4x4x3 array
arr3d = np.arange(1, 49).reshape(4, 4, 3)

print("\n4x4x3 Array:")
print(arr3d)

# Extract value at second set, first row and last column
value = arr3d[1, 0, -1]

print("\nExtracted Value:")
print(value)

# Create 4x4 array
arr4 = np.array([
    [11, 12, 13, 14],
    [15, 16, 17, 18],
    [19, 20, 21, 22],
    [23, 24, 25, 26]
])

print("\n4x4 Array:")
print(arr4)

# Extract odd rows and even columns
result = arr4[1::2, ::2]

print("\nOdd Rows and Even Columns:")
print(result)

# Slice first two rows and first two columns of second set
slice_array = arr3d[1, :2, :2]

print("\nSliced Array:")
print(slice_array)

# Replace odd numbers with -1 using for loop
arr_replace = np.array([
    [23, 56, 78, 93],
    [71, 82, 13, 24]
])

print("\nOriginal Array:")
print(arr_replace)

for i in range(arr_replace.shape[0]):
    for j in range(arr_replace.shape[1]):
        if arr_replace[i, j] % 2 != 0:
            arr_replace[i, j] = -1

print("\nArray after replacing odd numbers with -1:")
print(arr_replace)

# Get indices of non-zero elements
arr_nonzero = np.array([1, 0, 2, 0, 3, 0, 4])

indices = np.nonzero(arr_nonzero)

print("\nIndices of Non-Zero Elements:")
print(indices)

# Arithmetic operations
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

# Addition
print("\nAddition:")
print(a + b)

# Multiplication
print("\nMultiplication:")
print(a * b)

# Dot product
arr1 = np.array([15, 20, 25])
arr2 = np.array([10, 40, 37])

dot_product = np.dot(arr1, arr2)

print("\nDot Product:")
print(dot_product)

# End of program