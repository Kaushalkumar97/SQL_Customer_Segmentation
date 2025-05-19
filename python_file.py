import pandas as pd
import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="retail_db",
    user="postgres",
    password="Ammu@2498",
    host="localhost",
    port="5432"
)

# RFM segmentation SQL
query = """
WITH rfm_raw AS (
    SELECT 
        "CustomerID",
        DATE_PART('day', CURRENT_DATE - MAX("InvoiceDate")) AS recency,
        COUNT(DISTINCT "InvoiceNo") AS frequency,
        SUM("Quantity" * "UnitPrice") AS monetary
    FROM sales_data
    WHERE "CustomerID" IS NOT NULL
    GROUP BY "CustomerID"
),
rfm_scored AS (
    SELECT 
        "CustomerID",
        recency,
        frequency,
        monetary,
        NTILE(5) OVER (ORDER BY recency DESC) AS recency_score,
        NTILE(5) OVER (ORDER BY frequency) AS frequency_score,
        NTILE(5) OVER (ORDER BY monetary) AS monetary_score,
        NTILE(5) OVER (ORDER BY recency DESC)::TEXT ||
        NTILE(5) OVER (ORDER BY frequency)::TEXT ||
        NTILE(5) OVER (ORDER BY monetary)::TEXT AS rfm_score
    FROM rfm_raw
)
SELECT *,
    CASE 
        WHEN rfm_score = '555' THEN 'Top Customer'
        WHEN LEFT(rfm_score, 1) = '5' THEN 'Loyal Customer'
        WHEN SUBSTRING(rfm_score, 2, 1) = '5' THEN 'Frequent Buyer'
        WHEN RIGHT(rfm_score, 1) = '5' THEN 'Big Spender'
        WHEN rfm_score = '111' THEN 'Churned Customer'
        ELSE 'Regular Customer'
    END AS segment
FROM rfm_scored;
"""

# Export to CSV
df = pd.read_sql_query(query, conn)
df.to_csv("C:/Users/asus/OneDrive/Documents/Github_Projects/SQL_Customer_Segmentation/output/rfm_segment_sample.csv", index=False)

conn.close()
print("✅ CSV exported successfully!")
