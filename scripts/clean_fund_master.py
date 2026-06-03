import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

# Convert launch date
df["launch_date"] = pd.to_datetime(
    df["launch_date"],
    errors="coerce"
)

# Remove duplicates
df = df.drop_duplicates()

# Remove extra spaces
df.columns = df.columns.str.strip()

# Save
df.to_csv(
    "data/processed/fund_master_clean.csv",
    index=False
)

print("Fund Master cleaned successfully")