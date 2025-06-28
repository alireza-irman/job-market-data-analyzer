# Step 5: Visualization of salary distribution and job counts per province

import pandas as pd
import matplotlib.pyplot as plt

# Load the filtered data
file_path = r"D:\\AI\\Job Market Data Analyzer\\output\\filtered_jobs.csv"
df = pd.read_csv(file_path)

# Remove rows without Salary Minimum and copy
df_salary = df.dropna(subset=["Salary Minimum"]).copy()

# Convert salary columns to numeric
df_salary["Salary Minimum"] = pd.to_numeric(df_salary["Salary Minimum"], errors="coerce")

# Histogram of Salary Minimum
plt.figure(figsize=(8, 6))
plt.hist(df_salary["Salary Minimum"], bins=10, edgecolor="black")
plt.title("Salary Distribution (Minimum Salary)")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.grid(axis="y")
plt.tight_layout()
plt.savefig(r"D:\AI\Job Market Data Analyzer\output\salary_histogram.png")
plt.close()

print("✅ Salary histogram saved as 'salary_histogram.png'.")

# Bar chart of jobs per province
province_counts = df_salary["Province/Territory"].value_counts()

plt.figure(figsize=(8, 6))
province_counts.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Number of Jobs per Province")
plt.xlabel("Province")
plt.ylabel("Number of Jobs")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(r"D:\AI\Job Market Data Analyzer\output\province_job_counts.png")
plt.close()

print("✅ Province job counts bar chart saved as 'province_job_counts.png'.")
