#!/usr/bin/python3

# Import necessary libraries
import pandas as pd

# 1. Load the Dataset
# Load the dataset and preview the first few rows to understand its structure
file_path = 'your_dataset.csv'
df = pd.read_csv(file_path)
print("Initial Data Preview:")
print(df.head())

# 2. Identify and Handle Missing Values
# Check for missing values in each column
missing_values = df.isnull().sum()
print("\nMissing Values in Each Column:")
print(missing_values)


# 3. Standardize Data Types
# Convert data types as required (e.g., age as integer, enrollment_date as date)
df['age'] = df['age'].astype(int)
df['enrollment_date'] = pd.to_datetime(df['enrollment_date'], errors='coerce')

# 4. Normalize Text Data
# Standardize text data to title case for consistency
df['course_name'] = df['course_name'].str.title()

# 5. Filter Unwanted Data
# Remove rows where age is outside the realistic range of 18-45
df = df[(df['age'] >= 18) & (df['age'] <= 45)]

# 6. Correct Inconsistent Entries
# Standardize binary values (e.g., is_intern column)
df['is_intern'] = df['is_intern'].str.capitalize()

# 7. Save Cleaned Data
# Save the cleaned dataset to a new file
cleaned_file_path = 'cleaned_dataset.csv'
df.to_csv(cleaned_file_path, index=False)
print("\nData cleaning complete. Cleaned dataset saved to:", cleaned_file_path)
