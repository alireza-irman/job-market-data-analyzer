# Step 8: Compute IQR and create Box Plot of Minimum Salary

import pandas as pd
import matplotlib.pyplot as plt

# Load filtered dataset
file_path = r"D:\\AI\\Job Market Data Analyzer\\output\\filtered_jobs.csv"
df = pd.read_csv(file_path)

# Remove rows without Salary Minimum
df_salary = df.dropna(subset=["Salary Minimum"]).copy()

# Convert to numeric
df_salary["Salary Minimum"] = pd.to_numeric(df_salary["Salary Minimum"], errors="coerce")

# Compute quartiles
q1 = df_salary["Salary Minimum"].quantile(0.25)
q3 = df_salary["Salary Minimum"].quantile(0.75)
iqr = q3 - q1

# Identify outliers
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outliers = df_salary[(df_salary["Salary Minimum"] < lower_bound) | (df_salary["Salary Minimum"] > upper_bound)]

print("🔹 Q1:", round(q1, 2))
print("🔹 Q3:", round(q3, 2))
print("🔹 IQR:", round(iqr, 2))
print("🔹 Lower Bound:", round(lower_bound, 2))
print("🔹 Upper Bound:", round(upper_bound, 2))
print("🔹 Number of Outliers:", len(outliers))

# Create box plot
plt.figure(figsize=(6, 6))
plt.boxplot(df_salary["Salary Minimum"].dropna(), vert=True)
plt.title("Box Plot of Minimum Salary")
plt.ylabel("Salary")
plt.grid(True)
plt.tight_layout()
plt.savefig(r"D:\AI\Job Market Data Analyzer\output\boxplot_salary.png")
plt.close()

print("✅ Box plot saved as 'boxplot_salary.png'.")
