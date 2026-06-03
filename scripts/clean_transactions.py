import pandas as pd

df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

# Fix date
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

# Standardise values
df["transaction_type"] = (
    df["transaction_type"]
    .str.upper()
)

# Keep valid values
valid = [
    "SIP",
    "LUMPSUM",
    "REDEMPTION"
]

df = df[
    df["transaction_type"]
    .isin(valid)
]

# Amount > 0
df = df[
    df["amount_inr"] > 0
]

df.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)