import pandas as pd

df = pd.read_csv(
    "data/raw/05_category_inflows.csv"
)

df["month"] = pd.to_datetime(
    df["month"],
    errors="coerce"
)

df = df.drop_duplicates()

df.to_csv(
    "data/processed/category_inflows_clean.csv",
    index=False
)

print("Category inflows cleaned successfully")