# Step 1: Load dataset and preview columns and sample rows

import pandas as pd

# Define the file path to the dataset
file_path = r"D:\AI\Job Market Data Analyzer\data\job_postings_canada.csv"

# Read the CSV file using pandas
df = pd.read_csv(file_path)

# Print all column names
print("🟢 Columns:")
print(df.columns)

# Show the first 5 rows
print("\n🟢 Sample rows:")
print(df.head())

# Show the last 5 rows
print("\n🟢 Last rows:")
print(df.tail())
