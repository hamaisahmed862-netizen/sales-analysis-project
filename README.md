# 📊 Sales Analysis Project (Python + SQL + Power BI)

## 📌 Overview
This is an end-to-end data analytics project that analyzes sales data using Python, SQL, Excel, and Power BI.  
The goal is to extract meaningful business insights such as sales trends, profit analysis, discount impact, and category performance.

This project simulates a real-world data analyst workflow from raw data → cleaning → transformation → SQL analysis → visualization → dashboard creation.

---

## 🛠️ Tools & Technologies
- Python (Pandas, Matplotlib)
- SQL (SQLite)
- Power BI (Dashboarding & Visualization)
- Excel (Data exploration & reporting)
- Git & GitHub (Version control)

---

## 📂 Project Structure
sales-analysis-project/
│
├── dashboard.png
├── sqlqueries.sql
├── requirements.txt
├── README.md
│
├── data/
│ ├── raw/
│ ├── processed/
│
├── scripts/
│ └── load_to_sql.py
│
├── notebooks/
│ └── analysis.py
│
├── outputs/
│ ├── charts/
│ └── reports/
│
└── Excel/
└── Excel_dashboard.xlsx

---

## 🐍 Python Analysis (Notebooks)
Located in `notebooks/analysis.py`

### Work done:
- Data cleaning and preprocessing
- Handling missing values
- Exploratory Data Analysis (EDA)
- Sales trends over time
- Profit margin analysis
- Discount impact analysis

---

## 🗄️ SQL Analysis
Located in `sqlqueries.sql`

### Queries include:
- Sales by category
- Sales by year
- Profit analysis
- Discount impact on profit
- Aggregated business views

---

## ⚙️ Data Loading Script
Located in `scripts/load_to_sql.py`

### Purpose:
- Load raw CSV data into SQLite database
- Prepare data for SQL-based analysis

---

## 📊 Power BI Dashboard
File: `dashboard.png`

### Dashboard includes:
- KPI Cards (Total Sales, Profit, Profit Margin)
- Sales trend over time (Line chart)
- Category-wise performance (Bar chart)
- Discount impact visualization
- Interactive filters (slicers for year/category)

---

## 📈 Key Business Insights
- Technology category generates highest revenue
- Higher discounts significantly reduce profit margins
- Sales show steady growth trend over time
- Certain categories consistently outperform others in profitability

---

## 📊 Outputs Folder
- Charts generated using Python
- Analytical reports and summaries

---

## 📦 Excel Analysis
File: `Excel/excel_dash.xlsx`

- Contains additional exploratory analysis and dashboard support

---

## 🚀 How to Run This Project

1. Clone the repository:
```bash
git clone https://github.com/your-username/sales-analysis-project.git
