import pandas as pd

df = pd.read_csv(
    "data/raw/03_aum_by_fund_house.csv"
)

df["date"] = pd.to_datetime(
    df["date"],
    errors="coerce"
)

df = df.drop_duplicates()

df.to_csv(
    "data/processed/aum_by_fund_house_clean.csv",
    index=False
)

print("AUM data cleaned successfully")