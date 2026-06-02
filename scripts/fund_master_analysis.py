import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/01_fund_master.csv")

# Show all column names
print("Columns:")
print(df.columns)

print("\n" + "="*50)

# Unique fund houses
print("Fund Houses:")
print(df["fund_house"].unique())

print("\n" + "="*50)

# Unique categories
print("Categories:")
print(df["category"].unique())

print("\n" + "="*50)

# Unique sub categories
print("Sub Categories:")
print(df["sub_category"].unique())

print("\n" + "="*50)

# Unique risk categories
print("Risk Categories:")
print(df["risk_category"].unique())