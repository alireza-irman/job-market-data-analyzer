"""
Job Market Data Analyzer - Final Version

This script:
- Loads the dataset
- Cleans missing job titles
- Filters relevant jobs (Python/Data/AI)
- Computes salary statistics
- Generates visualization charts

Author: [Your Name]
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r"D:\\AI\\Job Market Data Analyzer\\data\\job_postings_canada.csv"
df = pd.read_csv(file_path)

# Clean missing job titles
df = df.dropna(subset=["Job Title"]).copy()

# Filter relevant jobs
keywords = [
    "Python Developer",
    "Data Analyst",
    "Data Engineer",
    "Machine Learning",
    "Artificial Intelligence",
    "AI Engineer",
    "AI Developer"
]
pattern = "|".join([fr"\b{k}\b" for k in keywords])

df = df[df["Job Title"].str.contains(pattern, case=False, na=False, regex=True)].copy()

# Convert salary columns to numeric
df["Salary Minimum"] = pd.to_numeric(df["Salary Minimum"], errors="coerce")

# Compute statistics
mean_salary = df["Salary Minimum"].mean()
median_salary = df["Salary Minimum"].median()

print("✅ Salary Statistics (Minimum Salary):")
print(f"Mean: {mean_salary:.2f}")
print(f"Median: {median_salary:.2f}")

# Count jobs per province
province_counts = df["Province/Territory"].value_counts()

print("\n✅ Number of jobs per province:")
print(province_counts)

# Save cleaned and filtered dataset
output_csv = r"D:\AI\Job Market Data Analyzer\output\final_filtered_jobs.csv"
df.to_csv(output_csv, index=False)
print(f"\n✅ Filtered dataset saved to {output_csv}")

# Create visualization - Salary Distribution
plt.figure(figsize=(8,6))
plt.hist(df["Salary Minimum"].dropna(), bins=10, edgecolor="black")
plt.title("Salary Distribution (Minimum Salary)")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(r"D:\AI\Job Market Data Analyzer\output\final_salary_histogram.png")
plt.close()
print("✅ Salary histogram saved.")

# Create visualization - Jobs per Province
plt.figure(figsize=(8,6))
province_counts.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Number of Jobs per Province")
plt.xlabel("Province")
plt.ylabel("Number of Jobs")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(r"D:\AI\Job Market Data Analyzer\output\final_province_job_counts.png")
plt.close()
print("✅ Province job counts bar chart saved.")
