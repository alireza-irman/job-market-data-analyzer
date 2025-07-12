
"""
Step 4: Compute mean and median salary
"""
import pandas as pd

def compute_salary_stats(df):
    df["Salary Minimum"] = pd.to_numeric(df["Salary Minimum"], errors="coerce")
    return df["Salary Minimum"].mean(), df["Salary Minimum"].median()

if __name__ == "__main__":
    from step3_filter_relevant_jobs import filter_relevant_jobs
    from step2_clean_data import clean_data
    from step1_load_data import load_data
    df = filter_relevant_jobs(clean_data(load_data("data/job_postings_canada.csv")))
    mean_salary, median_salary = compute_salary_stats(df)
    print(f"✅ Mean: {mean_salary:.2f}, Median: {median_salary:.2f}")
