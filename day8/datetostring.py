import pandas as pd

# Create a series of date strings
dates = pd.Series([
    '2026-05-01',
    '2026-05-02',
    '2026-05-03',
    '2026-05-04'
])

# Convert strings to datetime
timeseries = pd.to_datetime(dates)

# Display the time series
print(timeseries)


# pd.Series() creates a series of date strings.
# pd.to_datetime() converts the strings into datetime format.
# The resulting data type becomes datetime64[ns], which represents a time series in Pandas.