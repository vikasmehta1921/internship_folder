# Import libraries
import numpy as np


# Create first 2D array
arr1 = np.array([
    [10, 20],
    [30, 40]
])

# Create second 2D array
arr2 = np.array([
    [5, 15],
    [25, 35]
])

print("First Array:")
print(arr1)

print("\nSecond Array:")
print(arr2)

# Average of arrays
average = (arr1 + arr2) / 2

print("\nAverage of Arrays:")
print(average)

# Mean
mean_value = np.mean(average)

print("\nMean:")
print(mean_value)

# Median
median_value = np.median(average)

print("\nMedian:")
print(median_value)
