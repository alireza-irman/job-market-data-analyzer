# Step 3: Filter dataset for relevant jobs (More precise filtering)

import pandas as pd

# Define file path
file_path = r"D:\\AI\\Job Market Data Analyzer\\data\\job_postings_canada.csv"

# Read the CSV file
df = pd.read_csv(file_path)

# Drop rows without Job Title
df_cleaned = df.dropna(subset=["Job Title"])

# More precise keywords
keywords = [
    "Python Developer",
    "Data Analyst",
    "Data Engineer",
    "Machine Learning",
    "Artificial Intelligence",
    "AI Engineer",
    "AI Developer"
]

# Create regex pattern with word boundaries
pattern = "|".join([fr"\b{k}\b" for k in keywords])

# Filter jobs
df_filtered = df_cleaned[df_cleaned["Job Title"].str.contains(pattern, case=False, na=False, regex=True)]

# Show number of filtered rows
print("🔹 Total relevant jobs found:", len(df_filtered))

# Show sample rows
print("\n🔹 Sample relevant jobs:")
print(df_filtered[["Job Title", "City", "Province/Territory", "Salary Minimum", "Salary Maximum"]].head())

# Save filtered data to CSV
output_path = r"D:\AI\Job Market Data Analyzer\output\filtered_jobs.csv"
df_filtered.to_csv(output_path, index=False)
