
"""
Step 9: Normalize salaries using Min-Max scaling
"""
import pandas as pd

def normalize_salaries(df):
    df["Salary Minimum"] = pd.to_numeric(df["Salary Minimum"], errors="coerce")
    s = df["Salary Minimum"].dropna()
    df = df.loc[s.index]
    df["Normalized"] = (s - s.min()) / (s.max() - s.min())
    return df

if __name__ == "__main__":
    from step3_filter_relevant_jobs import filter_relevant_jobs
    from step2_clean_data import clean_data
    from step1_load_data import load_data
    df = filter_relevant_jobs(clean_data(load_data("data/job_postings_canada.csv")))
    df = normalize_salaries(df)
    df.to_csv("output/normalized_salaries.csv", index=False)
    print("✅ Normalized salaries saved.")
