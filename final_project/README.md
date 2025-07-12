
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
pip install -r requirements.txt
```

Run the main script:

```
python main.py
```

You can also run each learning step separately (if provided):

```
python step1_load_data.py
...
python step9_normalization.py
```

---

## 📂 Project Structure

```
job_market_data_analyzer/
├── data/
│   └── job_postings_canada.csv
├── main.py
├── requirements.txt
├── output/
│   └── final_filtered_jobs.csv
│   └── final_salary_histogram.png
│   └── final_province_job_counts.png
```

---

## 📈 Outputs

- Filtered dataset as CSV
- Histogram of salary distribution
- Bar chart of job count per province

---

## 🧠 Key Libraries Used

- `pandas` for data handling
- `matplotlib` for visualization
- `scipy` for statistical analysis

---

## ✨ Author

Created by **Alireza Ahmadi Dehnavi**  
As part of a migration-ready learning portfolio in **Python & AI**  


License: MIT
