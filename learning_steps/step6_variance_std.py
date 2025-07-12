
"""
Step 6: Compute variance and standard deviation
"""
import pandas as pd

def compute_dispersion(df):
    df["Salary Minimum"] = pd.to_numeric(df["Salary Minimum"], errors="coerce")
    return df["Salary Minimum"].var(), df["Salary Minimum"].std()

if __name__ == "__main__":
    from step3_filter_relevant_jobs import filter_relevant_jobs
    from step2_clean_data import clean_data
    from step1_load_data import load_data
    df = filter_relevant_jobs(clean_data(load_data("data/job_postings_canada.csv")))
    var, std = compute_dispersion(df)
    print(f"✅ Variance: {var:.2f}, Std Dev: {std:.2f}")
