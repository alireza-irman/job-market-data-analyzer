# 📊 Job Market Data Analyzer

This project analyzes Canadian job postings related to **Python**, **Data**, and **Artificial Intelligence**.

It includes:
- Data cleaning
- Filtering relevant jobs
- Salary statistics computation
- Statistical analysis (variance, skewness, IQR, normalization)
- Visualization charts

---

## 🚀 How to Run

Make sure you have **Python 3.x** installed.

Install dependencies:
```
pip install pandas matplotlib
```

Run the main script:
```
python final_project/main.py
```

You can also run each learning step separately:
```
python learning_steps/step1_load_data.py
...
python learning_steps/step9_normalization.py
```

---

## 📂 Project Structure

```
job_market_data_analyzer/
├── data/
│   └── job_postings_canada.csv
├── learning_steps/
│   └── step1_load_data.py
│   └── step2_clean_data.py
│   └── step3_filter_relevant_jobs.py
│   └── step4_salary_statistics.py
│   └── step5_visualization.py
│   └── step6_variance_std.py
│   └── step7_skewness_kurtosis.py
│   └── step8_boxplot_iqr.py
│   └── step9_normalization.py
├── final_project/
│   └── main.py
│   └── README.md
├── output/
│   └── final_filtered_jobs.csv
│   └── final_salary_histogram.png
│   └── final_province_job_counts.png
│   └── boxplot_salary.png
│   └── normalized_salaries.csv
├── requirements.txt
```

---

## 📈 Outputs

After running `main.py` and the learning steps, you will find:

- **Filtered Dataset:**
  - `output/final_filtered_jobs.csv`
- **Salary Histogram:**
  - `output/final_salary_histogram.png`
- **Province Job Counts Bar Chart:**
  - `output/final_province_job_counts.png`
- **Box Plot of Salaries:**
  - `output/boxplot_salary.png`
- **Normalized Salaries:**
  - `output/normalized_salaries.csv`

---

## 🧠 Key Libraries Used

- `pandas` for data handling
- `matplotlib` for visualization

---

## ✨ Author

Created by Alireza Ahmadi Dehnavi as part of a public learning journey into Python and AI.


---
