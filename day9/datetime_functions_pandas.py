# Import libraries
import pandas as pd
import numpy as np

# Create date range
dates = pd.date_range(start="2026-01-01", periods=5, freq='D')

print(dates)

# Create dataframe
df = pd.DataFrame({
    'Date': pd.date_range(start='2026-01-01', periods=5, freq='D'),
    'Sales': [1000, 1200, 1500, 1800, 2000]
})

print(df)

# Convert string to datetime
df['Date'] = pd.to_datetime(df['Date'])

print(df.dtypes)

# Extract year, month and day
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

print(df)

# Find day name
df['Day_Name'] = df['Date'].dt.day_name()

print(df[['Date', 'Day_Name']])

# Find month name
df['Month_Name'] = df['Date'].dt.month_name()

print(df[['Date', 'Month_Name']])

# Find weekday number
df['Weekday_Number'] = df['Date'].dt.weekday

print(df[['Date', 'Weekday_Number']])

# Check weekend
df['Is_Weekend'] = df['Weekday_Number'] >= 5

print(df[['Date', 'Is_Weekend']])

# Current date and time
current_datetime = pd.Timestamp.now()

print(current_datetime)

# Date difference
start_date = pd.to_datetime("2026-01-01")
end_date = pd.to_datetime("2026-02-01")

difference = end_date - start_date

print(difference)

# Add 7 days
df['Next_7_Days'] = df['Date'] + pd.Timedelta(days=7)

print(df[['Date', 'Next_7_Days']])

# Subtract 7 days
df['Previous_7_Days'] = df['Date'] - pd.Timedelta(days=7)

print(df[['Date', 'Previous_7_Days']])

# Filter data
filtered_data = df[df['Date'] > '2026-01-03']

print(filtered_data)

# Sort dataframe
sorted_df = df.sort_values(by='Date', ascending=False)

print(sorted_df)

# Set date as index
df_index = df.set_index('Date')

print(df_index)

# Monthly resampling
monthly_sales = df_index['Sales'].resample('M').sum()

print(monthly_sales)

# Hourly timestamps
hours = pd.date_range(start='2026-01-01', periods=5, freq='H')

print(hours)

# Format date
df['Formatted_Date'] = df['Date'].dt.strftime('%d-%m-%Y')

print(df[['Date', 'Formatted_Date']])

# Find quarter
df['Quarter'] = df['Date'].dt.quarter

print(df[['Date', 'Quarter']])

# Days in month
df['Days_In_Month'] = df['Date'].dt.days_in_month

print(df[['Date', 'Days_In_Month']])

# Create time series
time_series = pd.Series(
    [100, 200, 300, 400],
    index=pd.date_range('2026-01-01', periods=4)
)

print(time_series)

# Rolling average
df['Rolling_Avg'] = df['Sales'].rolling(window=2).mean()

print(df[['Sales', 'Rolling_Avg']])

# Shift dates
df['Shifted_Date'] = df['Date'].shift(1)

print(df[['Date', 'Shifted_Date']])

# Timezone conversion
utc_time = pd.Timestamp.now(tz='UTC')

india_time = utc_time.tz_convert('Asia/Kolkata')

print(utc_time)
print(india_time)

# Minimum and maximum date
print(df['Date'].min())
print(df['Date'].max())

# Check null dates
df.loc[2, 'Date'] = np.nan

print(df['Date'].isnull())

# Fill null dates
df['Date'] = df['Date'].fillna(method='ffill')

print(df['Date'])

# Date offset
new_date = pd.Timestamp('2026-01-01') + pd.DateOffset(months=2)

print(new_date)

# Business days
business_days = pd.bdate_range(start='2026-01-01', periods=5)

print(business_days)

# Unix timestamp
timestamp = pd.Timestamp('2026-01-01').timestamp()

print(timestamp)

# End of program