import pandas as pd

df = pd.read_csv(
    "data/raw/09_portfolio_holdings.csv"
)

df["portfolio_date"] = pd.to_datetime(
    df["portfolio_date"],
    errors="coerce"
)

df = df[
    (df["weight_pct"] >= 0)
    &
    (df["weight_pct"] <= 100)
]

df = df.drop_duplicates()

df.to_csv(
    "data/processed/portfolio_holdings_clean.csv",
    index=False
)

print("Portfolio holdings cleaned successfully")