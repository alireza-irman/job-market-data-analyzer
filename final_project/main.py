
"""
Job Market Data Analyzer - Final Script
Author: Alireza Ahmadi Dehnavi

Performs:
- Load and clean job postings
- Filter Python/Data/AI jobs
- Compute salary stats
- Visualize and export results
"""

import pandas as pd
import matplotlib.pyplot as plt
import os
from pathlib import Path

DATA_PATH = Path("data/job_postings_canada.csv")
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def load_and_clean_data(path):
    df = pd.read_csv(path)
    df = df.dropna(subset=["Job Title"]).copy()
    return df

def filter_relevant_jobs(df):
    keywords = [
        "Python Developer", "Data Analyst", "Data Engineer",
        "Machine Learning", "Artificial Intelligence", "AI Engineer", "AI Developer"
    ]
    pattern = "|".join([fr"\b{k}\b" for k in keywords])
    return df[df["Job Title"].str.contains(pattern, case=False, na=False, regex=True)].copy()

def compute_statistics(df):
    df["Salary Minimum"] = pd.to_numeric(df["Salary Minimum"], errors="coerce")
    mean_salary = df["Salary Minimum"].mean()
    median_salary = df["Salary Minimum"].median()
    return mean_salary, median_salary

def save_outputs(df, mean_salary, median_salary):
    df.to_csv(OUTPUT_DIR / "final_filtered_jobs.csv", index=False)
    print(f"✅ Filtered dataset saved to {OUTPUT_DIR / 'final_filtered_jobs.csv'}")

    # Histogram
    plt.figure(figsize=(8,6))
    plt.hist(df["Salary Minimum"].dropna(), bins=10, edgecolor="black")
    plt.title("Salary Distribution (Minimum Salary)")
    plt.xlabel("Salary")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "final_salary_histogram.png")
    plt.close()

    # Province bar chart
    plt.figure(figsize=(8,6))
    df["Province/Territory"].value_counts().plot(kind="bar", color="skyblue", edgecolor="black")
    plt.title("Number of Jobs per Province")
    plt.xlabel("Province")
    plt.ylabel("Number of Jobs")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "final_province_job_counts.png")
    plt.close()
    print("✅ Visualizations saved.")

    # Print summary
    print("✅ Salary Statistics (Minimum Salary):")
    print(f"Mean: {mean_salary:.2f}")
    print(f"Median: {median_salary:.2f}")

def main():
    df = load_and_clean_data(DATA_PATH)
    df = filter_relevant_jobs(df)
    mean_salary, median_salary = compute_statistics(df)
    save_outputs(df, mean_salary, median_salary)

if __name__ == "__main__":
    main()
