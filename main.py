import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# LOAD DATA
# ---------------------------
try:
    df = pd.read_csv('sales_data.csv')
    print("Data loaded successfully!")
except:
    print("Error loading file!")
    exit()

# ---------------------------
# DATA CLEANING
# ---------------------------
df['Date'] = pd.to_datetime(df['Date'])

if df.isnull().sum().sum() > 0:
    df.fillna(0, inplace=True)

df['Month'] = df['Date'].dt.to_period('M')

# ---------------------------
# ANALYSIS
# ---------------------------
monthly_sales = df.groupby('Month')['Total_Sales'].sum()
top_products = df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False).head(5)
region_sales = df.groupby('Region')['Total_Sales'].sum()
monthly_growth = monthly_sales.pct_change() * 100

# ---------------------------
# 📈 CHART 1
# ---------------------------
plt.figure()
monthly_sales.plot(kind='line')
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

# ---------------------------
# 📊 CHART 2
# ---------------------------
plt.figure()
top_products.plot(kind='bar')
plt.title("Top 5 Products by Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

# ---------------------------
# 🥧 CHART 3
# ---------------------------
plt.figure()
region_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title("Region-wise Sales Share")
plt.ylabel("")
plt.show()

# ---------------------------
# 📉 CHART 4
# ---------------------------
plt.figure()
monthly_growth.plot(kind='line')
plt.title("Monthly Growth Rate (%)")
plt.xlabel("Month")
plt.ylabel("Growth %")
plt.tight_layout()
plt.show()

print("\n✅ Charts displayed successfully!")
