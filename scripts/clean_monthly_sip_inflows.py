import pandas as pd

df = pd.read_csv(
    "data/raw/04_monthly_sip_inflows.csv"
)

df["month"] = pd.to_datetime(
    df["month"],
    errors="coerce"
)

df["yoy_growth_pct"] = (
    df["yoy_growth_pct"]
    .fillna(0)
)

df = df.drop_duplicates()

df.to_csv(
    "data/processed/monthly_sip_inflows_clean.csv",
    index=False
)

print("SIP inflows cleaned successfully")