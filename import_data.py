import pandas as pd
import psycopg2

# Load CSV from your GitHub folder
df = pd.read_csv("C:/Users/asus/OneDrive/Documents/Github_Projects/SQL_Customer_Segmentation/data.csv", encoding='ISO-8859-1')

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="retail_db",
    user="postgres",
    password="Ammu@2498", 
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Insert each row into the sales_data table
for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO sales_data("InvoiceNo", "StockCode", "Description", "Quantity", "InvoiceDate", "UnitPrice", "CustomerID", "Country")
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, tuple(row))

conn.commit()
cur.close()
conn.close()

print("✅ Data inserted successfully!")
