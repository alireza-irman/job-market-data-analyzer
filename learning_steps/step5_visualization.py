
"""
Step 5: Visualize salary distribution
"""
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def plot_salary_histogram(df, output_path):
    df["Salary Minimum"] = pd.to_numeric(df["Salary Minimum"], errors="coerce")
    plt.figure(figsize=(8,6))
    plt.hist(df["Salary Minimum"].dropna(), bins=10, edgecolor="black")
    plt.title("Salary Distribution")
    plt.xlabel("Salary")
    plt.ylabel("Frequency")
    plt.tight_layout()
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path)
    plt.close()

if __name__ == "__main__":
    from step3_filter_relevant_jobs import filter_relevant_jobs
    from step2_clean_data import clean_data
    from step1_load_data import load_data
    df = filter_relevant_jobs(clean_data(load_data("data/job_postings_canada.csv")))
    plot_salary_histogram(df, "output/salary_histogram.png")
    print("✅ Histogram saved.")
