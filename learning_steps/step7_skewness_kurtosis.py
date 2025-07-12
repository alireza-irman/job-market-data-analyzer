
"""
Step 7: Compute skewness and kurtosis
"""
import pandas as pd
from scipy.stats import skew, kurtosis

def compute_shape(df):
    df["Salary Minimum"] = pd.to_numeric(df["Salary Minimum"], errors="coerce")
    return skew(df["Salary Minimum"].dropna()), kurtosis(df["Salary Minimum"].dropna())

if __name__ == "__main__":
    from step3_filter_relevant_jobs import filter_relevant_jobs
    from step2_clean_data import clean_data
    from step1_load_data import load_data
    df = filter_relevant_jobs(clean_data(load_data("data/job_postings_canada.csv")))
    s, k = compute_shape(df)
    print(f"✅ Skewness: {s:.2f}, Kurtosis: {k:.2f}")
