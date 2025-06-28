# Step 9: Normalize Minimum Salary to [0, 1] range

import pandas as pd

# Load filtered dataset
file_path = r"D:\\AI\\Job Market Data Analyzer\\output\\filtered_jobs.csv"
df = pd.read_csv(file_path)

# Remove rows without Salary Minimum
df_salary = df.dropna(subset=["Salary Minimum"]).copy()

# Convert to numeric
df_salary["Salary Minimum"] = pd.to_numeric(df_salary["Salary Minimum"], errors="coerce")

# Compute min and max
salary_min = df_salary["Salary Minimum"].min()
salary_max = df_salary["Salary Minimum"].max()

# Apply normalization
df_salary["Normalized Salary"] = (df_salary["Salary Minimum"] - salary_min) / (salary_max - salary_min)

# Show sample
print("🔹 Sample normalized salaries:")
print(df_salary[["Salary Minimum", "Normalized Salary"]].head())

# Save to CSV
output_path = r"D:\AI\Job Market Data Analyzer\output\normalized_salaries.csv"
df_salary.to_csv(output_path, index=False)

print("✅ Normalized salaries saved as 'normalized_salaries.csv'.")
