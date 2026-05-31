# Import numpy
import numpy as np

# Create array with NaN values
arr = np.array([
    [10, 20, np.nan],
    [40, np.nan, 60],
    [70, 80, 90]
])

print("Original Array:")
print(arr)

# Find column averages ignoring NaN
col_mean = np.nanmean(arr, axis=0)

# Find indices of NaN values
indices = np.where(np.isnan(arr))

# Replace NaN with column average
arr[indices] = np.take(col_mean, indices[1])

print("\nArray after replacing NaN with column average:")
print(arr)