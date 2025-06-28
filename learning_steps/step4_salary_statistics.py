# Step 4: Salary statistics and summary analysis

import pandas as pd

# Define file path
file_path = r"D:\\AI\\Job Market Data Analyzer\\output\\filtered_jobs.csv"

# Read the filtered dataset
df = pd.read_csv(file_path)

# Remove rows without salary info (at least Salary Minimum)
df_salary = df.dropna(subset=["Salary Minimum"]).copy()

# Convert salary columns to numeric (if needed)
df_salary["Salary Minimum"] = pd.to_numeric(df_salary["Salary Minimum"], errors="coerce")
df_salary["Salary Maximum"] = pd.to_numeric(df_salary["Salary Maximum"], errors="coerce")

# Compute statistics
mean_salary_min = df_salary["Salary Minimum"].mean()
median_salary_min = df_salary["Salary Minimum"].median()
max_salary_min = df_salary["Salary Minimum"].max()
min_salary_min = df_salary["Salary Minimum"].min()

# Show statistics
print("🔹 Salary Statistics (Minimum Salary):")
print(f"Mean: {mean_salary_min:.2f}")
print(f"Median: {median_salary_min:.2f}")
print(f"Min: {min_salary_min:.2f}")
print(f"Max: {max_salary_min:.2f}")

# Count jobs per province
province_counts = df_salary["Province/Territory"].value_counts()

print("\n🔹 Number of jobs per province:")
print(province_counts)
