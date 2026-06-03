import pandas as pd

df = pd.read_csv(
    "data/raw/06_industry_folio_count.csv"
)

df["month"] = pd.to_datetime(
    df["month"],
    errors="coerce"
)

df = df.drop_duplicates()

df.to_csv(
    "data/processed/industry_folio_count_clean.csv",
    index=False
)

print("Industry folio count cleaned successfully")