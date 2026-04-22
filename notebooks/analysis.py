import pandas as pd
import matplotlib.pyplot as plt

# ---------------- SETTINGS ---------------- #
pd.set_option('display.float_format', '{:,.2f}'.format)

# ---------------- LOAD DATA ---------------- #
df = pd.read_csv(
    r'C:\Users\HP\OneDrive\Documents\sales-analysis-project\data\raw\Global_Superstore2.csv',
    encoding='latin-1'
)

# ---------------- BASIC CHECK ---------------- #
print(df.head())
df.info()

# ---------------- DATA CLEANING ---------------- #

# Convert numeric columns
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
df['Profit'] = pd.to_numeric(df['Profit'], errors='coerce')
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df['Discount'] = pd.to_numeric(df['Discount'], errors='coerce')

# Convert date columns
df['Order_Date'] = pd.to_datetime(df['Order_Date'], dayfirst=True)
df['Ship_Date'] = pd.to_datetime(df['Ship_Date'], dayfirst=True)

# Fix column names
df.columns = df.columns.str.strip().str.replace(" ", "_").str.replace("-", "_")

# Clean text columns
text_cols = ['Category', 'Sub_Category', 'Region', 'Segment', 'Product_Name']
for col in text_cols:
    df[col] = df[col].astype(str).str.strip().str.title()

# Handle missing values
df = df.fillna(0)

# ---------------- FEATURE ENGINEERING ---------------- #

df['Profit_Margin'] = df['Profit'] / df['Sales']
df['Year'] = df['Order_Date'].dt.year
df['Month'] = df['Order_Date'].dt.month

# ---------------- ANALYSIS ---------------- #

sales_by_category = df.groupby('Category')['Sales'].sum()
print("\nSales by Category:")
print(sales_by_category)

profit_by_category = df.groupby('Category')['Profit'].sum()
print("\nProfit by Category:")
print(profit_by_category)

profit_margin_by_category = df.groupby('Category')['Profit_Margin'].mean()
print("\nProfit Margin by Category:")
print(profit_margin_by_category)

discount_profit = df.groupby('Discount')['Profit'].mean()
print("\nDiscount vs Profit:")
print(discount_profit)

top_products = df.groupby('Product_Name')['Sales'].sum().sort_values(ascending=False).head(10)
print("\nTop Products:")
print(top_products)

sales_by_year = df.groupby('Year')['Sales'].sum() / 1_000_000
print("\nSales by Year (Millions):")
print(sales_by_year)

sales_by_region = df.groupby('Region')['Sales'].sum()
print("\nSales by Region:")
print(sales_by_region)

# ---------------- VISUALIZATION ---------------- #

# Sales by Category
plt.figure()
sales_by_category.plot(kind='bar')
plt.title('Sales by Category')
plt.xlabel('Category')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.savefig(r'C:\Users\HP\OneDrive\Documents\sales-analysis-project\outputs\charts\sales_by_category.png')
plt.show()

# Profit by Category
plt.figure()
profit_by_category.plot(kind='bar')
plt.title('Profit by Category')
plt.xlabel('Category')
plt.ylabel('Profit')
plt.xticks(rotation=45)
plt.savefig(r'C:\Users\HP\OneDrive\Documents\sales-analysis-project\outputs\charts\profit_by_category.png')
plt.show()

# Sales Trend Over Years
plt.figure()
sales_by_year.plot(kind='line', marker='o')
plt.title('Sales Trend Over Years (in Millions)')
plt.xlabel('Year')
plt.ylabel('Sales (Millions)')
plt.xticks(sales_by_year.index)
plt.grid(True)

plt.savefig(r'C:\Users\HP\OneDrive\Documents\sales-analysis-project\outputs\charts\sales_trend_over_years.png')
plt.show()

# ---------------- SAVE CLEAN DATA ---------------- #

df.to_csv(
    r'C:\Users\HP\OneDrive\Documents\sales-analysis-project\data\processed\cleaned_data.csv',
    index=False
)