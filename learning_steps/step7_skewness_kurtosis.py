# Step 7: Compute Skewness and Kurtosis of Minimum Salary

import pandas as pd

# Load filtered dataset
file_path = r"D:\\AI\\Job Market Data Analyzer\\output\\filtered_jobs.csv"
df = pd.read_csv(file_path)

# Remove rows without Salary Minimum
df_salary = df.dropna(subset=["Salary Minimum"]).copy()

# Convert to numeric
df_salary["Salary Minimum"] = pd.to_numeric(df_salary["Salary Minimum"], errors="coerce")

# Compute skewness and kurtosis
skewness = df_salary["Salary Minimum"].skew()
kurtosis = df_salary["Salary Minimum"].kurt()

print("🔹 Skewness of Minimum Salary:", round(skewness, 2))
print("🔹 Kurtosis of Minimum Salary:", round(kurtosis, 2))
