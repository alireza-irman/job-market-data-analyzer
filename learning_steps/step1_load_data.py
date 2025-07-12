
"""
Step 1: Load job data from CSV
"""
import pandas as pd
from pathlib import Path

def load_data(path):
    df = pd.read_csv(path)
    print(f"✅ Loaded {len(df)} rows.")
    return df

if __name__ == "__main__":
    df = load_data(Path("data/job_postings_canada.csv"))
    print(df.head())
