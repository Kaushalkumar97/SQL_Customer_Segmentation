
# 📊 SQL Customer Segmentation using RFM Analysis

This project applies RFM (Recency, Frequency, Monetary) analysis using SQL and visualizes the results in Power BI to segment retail customers into strategic categories like Top Customers, Loyal Customers, and Churned Customers.

---

## 🎯 Objectives

- Import and clean e-commerce transaction data
- Segment customers using RFM scoring logic in PostgreSQL
- Export segmented data to CSV
- Visualize key KPIs and customer groups in Power BI

---

## 🧠 RFM Explained

| Metric     | Description                          |
|------------|--------------------------------------|
| Recency    | Days since the last purchase         |
| Frequency  | Number of unique purchase invoices   |
| Monetary   | Total value spent by the customer    |

RFM scores (1-5) are assigned using SQL window functions (`NTILE`). The scores are concatenated to form an `rfm_score` (e.g., 555) and then mapped to customer segments.

---

## 🗂️ Project Structure

```
SQL_Customer_Segmentation/
├── data.csv                        # Raw transaction data
├── import_data.py                 # Inserts data into PostgreSQL
├── python_file.py                 # Extracts RFM segments and exports to CSV
├── rfm_segment_sample.csv         # Exported segmented data
├── SQL_Dashboard.pbix             # Power BI dashboard file
└── README.md                      # Project documentation
```

---

## ⚙️ Tools Used

- PostgreSQL (pgAdmin)
- Python (pandas, psycopg2)
- Power BI
- SQL (NTILE, CASE, Aggregation)

---

## 📊 Power BI Dashboard Highlights

- **Donut Chart** – Customer segment distribution
- **Bar Chart** – Avg spend per segment
- **Table** – Top 50 customers by spend
- **KPI Cards**:
  - 💰 Total Revenue
  - 🧾 Average Order Value
  - 🔻 Churned Customers
  - 📉 Churn Rate
  - 🟢 Loyal Customers %
  - 🔁 Repeat Buyer Rate

---

## ▶️ How to Reproduce

1. **Import Data to PostgreSQL**
   - Edit `import_data.py` if needed and run it.

2. **Generate RFM Segments**
   - Run `python_file.py` to export `rfm_segment_sample.csv`.

3. **Open Power BI Dashboard**
   - Use `SQL_Dashboard.pbix` and refresh the data source if needed.

---

## 📌 Segment Definitions

| RFM Score | Segment            |
|-----------|--------------------|
| 555       | ⭐ Top Customer     |
| 5XX       | 🟢 Loyal Customer   |
| X5X       | 🟡 Frequent Buyer   |
| XX5       | 💰 Big Spender      |
| 111       | 🔴 Churned Customer |
| Others    | 🧍 Regular Customer |

---

## 🙌 Author

Created by **[Your Name]** as part of a hands-on SQL + BI learning project.

