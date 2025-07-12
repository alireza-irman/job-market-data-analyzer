
"""
Step 8: Generate boxplot and calculate IQR
"""
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def boxplot_and_iqr(df, output_path):
    df["Salary Minimum"] = pd.to_numeric(df["Salary Minimum"], errors="coerce")
    q1 = df["Salary Minimum"].quantile(0.25)
    q3 = df["Salary Minimum"].quantile(0.75)
    iqr = q3 - q1
    plt.figure(figsize=(6,4))
    plt.boxplot(df["Salary Minimum"].dropna(), vert=False)
    plt.title("Salary Boxplot")
    plt.tight_layout()
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path)
    plt.close()
    return iqr

if __name__ == "__main__":
    from step3_filter_relevant_jobs import filter_relevant_jobs
    from step2_clean_data import clean_data
    from step1_load_data import load_data
    df = filter_relevant_jobs(clean_data(load_data("data/job_postings_canada.csv")))
    iqr = boxplot_and_iqr(df, "output/boxplot_salary.png")
    print(f"✅ IQR: {iqr:.2f}")
