
"""
Step 2: Clean missing job titles
"""
import pandas as pd

def clean_data(df):
    return df.dropna(subset=["Job Title"]).copy()

if __name__ == "__main__":
    from step1_load_data import load_data
    df = load_data("data/job_postings_canada.csv")
    cleaned = clean_data(df)
    print(f"✅ Cleaned dataset has {len(cleaned)} rows.")
