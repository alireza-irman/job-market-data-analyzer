# Step 6: Compute Variance and Standard Deviation of Minimum Salary

import pandas as pd

# Load filtered dataset
file_path = r"D:\\AI\\Job Market Data Analyzer\\output\\filtered_jobs.csv"
df = pd.read_csv(file_path)

# Remove rows without Salary Minimum
df_salary = df.dropna(subset=["Salary Minimum"]).copy()

# Convert to numeric
df_salary["Salary Minimum"] = pd.to_numeric(df_salary["Salary Minimum"], errors="coerce")

# Compute statistics
variance = df_salary["Salary Minimum"].var()
std_dev = df_salary["Salary Minimum"].std()

print("🔹 Variance of Minimum Salary:", round(variance, 2))
print("🔹 Standard Deviation of Minimum Salary:", round(std_dev, 2))
