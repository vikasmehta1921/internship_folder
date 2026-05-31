# Import libraries
import pandas as pd
import numpy as np

# Load CSV file
df = pd.read_csv(r"C:\Users\vinay\OneDrive\Desktop\internship_folder-main\day9\tips.csv")

# Display first 5 rows
print("First 5 Rows")
print(df.head())

# Dataset information
print("\nDataset Information")
print(df.info())

# Check missing values
print("\nMissing Values")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows")
print(df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing numeric values with mean
numeric_columns = df.select_dtypes(include=np.number).columns

df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())

# Fill missing categorical values with mode
categorical_columns = df.select_dtypes(include='object').columns

# Fill missing categorical values with mode using vectorized operation
df[categorical_columns] = df[categorical_columns].fillna(df[categorical_columns].mode().iloc[0])
# Check missing values after cleaning
print("\nMissing Values After Cleaning")
print(df.isnull().sum())

# Statistical summary
print("\nStatistical Summary")
print(df.describe())

# Display column names
print("\nColumn Names")
print(list(df.columns))

# Total bill amount
print("\nTotal Bill Amount")
print(df['total_bill'].sum())

# Average tip
print("\nAverage Tip")
print(df['tip'].mean())

# Maximum tip
print("\nMaximum Tip")
print(df['tip'].max())

# Minimum tip
print("\nMinimum Tip")
print(df['tip'].min())

# Average total bill
print("\nAverage Total Bill")
print(df['total_bill'].mean())

# Gender wise average tip
print("\nGender Wise Average Tip")
print(df.groupby('sex')['tip'].mean())

# Day wise total bill
print("\nDay Wise Total Bill")
print(df.groupby('day')['total_bill'].sum())

# Smoker vs non-smoker average tip
print("\nSmoker vs Non-Smoker Average Tip")
print(df.groupby('smoker')['tip'].mean())

# Time wise average bill
print("\nLunch/Dinner Average Bill")
print(df.groupby('time')['total_bill'].mean())

# Highest bill record
highest_bill = df[df['total_bill'] == df['total_bill'].max()]

print("\nHighest Bill Record")
print(highest_bill)

# Create tip percentage column
df['tip_percentage'] = (df['tip'] / df['total_bill']) * 100

print("\nTip Percentage")
print(df[['total_bill', 'tip', 'tip_percentage']].head())

# Customers giving more than 20% tip
high_tippers = df[df['tip_percentage'] > 20]

print("\nCustomers Giving More Than 20% Tip")
print(high_tippers)

# Correlation matrix
print("\nCorrelation Matrix")
import pandas as pd
from packaging import version

if version.parse(pd.__version__) >= version.parse("1.5.0"):
	print(df.corr(numeric_only=True))
else:
	print(df.corr())

# Sort by highest tip
sorted_tips = df.sort_values(by='tip', ascending=False)

print("\nTop 10 Highest Tips")
print(sorted_tips.head(10))

# Count customers by day
print("\nCustomer Count By Day")
print(df['day'].value_counts())

# Count customers by gender
print("\nCustomer Count By Gender")
print(df['sex'].value_counts())

# Count smokers and non-smokers
print("\nSmoker Count")
# Save cleaned dataset for future analysis or sharing
df.to_csv("cleaned_tips.csv", index=False)

print("\nCleaned dataset saved successfully")
print(df['tip_percentage'].mean())

# Save cleaned dataset
df.to_csv("cleaned_tips.csv", index=False)

print("\nCleaned dataset saved successfully")

# End of program