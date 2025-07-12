
"""
Step 3: Filter Python/Data/AI jobs
"""
import pandas as pd

def filter_relevant_jobs(df):
    keywords = [
        "Python Developer", "Data Analyst", "Data Engineer",
        "Machine Learning", "Artificial Intelligence", "AI Engineer", "AI Developer"
    ]
    pattern = "|".join([fr"\b{k}\b" for k in keywords])
    return df[df["Job Title"].str.contains(pattern, case=False, na=False, regex=True)].copy()

if __name__ == "__main__":
    from step2_clean_data import clean_data
    from step1_load_data import load_data
    df = load_data("data/job_postings_canada.csv")
    df = clean_data(df)
    filtered = filter_relevant_jobs(df)
    print(f"✅ {len(filtered)} relevant jobs found.")
