# Step 2: Clean dataset by dropping rows without Job Title

import pandas as pd

# Define file path
file_path = r"D:\AI\Job Market Data Analyzer\data\job_postings_canada.csv"

# Read the CSV file
df = pd.read_csv(file_path)



df_cleaned_salary = df.dropna(subset=["Salary Minimum"])
print("Rows with Salary Minimum:", len(df_cleaned_salary))
