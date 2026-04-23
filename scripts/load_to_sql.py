import pandas as pd
import sqlite3

# Load cleaned data
df = pd.read_csv(r'C:\Users\HP\OneDrive\Documents\sales-analysis-project\data\processed\cleaned_data.csv')

# Create database
conn = sqlite3.connect(r'C:\Users\HP\OneDrive\Documents\sales-analysis-project\sales.db')

# Load data into SQL table
df.to_sql('sales', conn, if_exists='replace', index=False)

print(" Data successfully loaded into SQL database!")

conn.close()