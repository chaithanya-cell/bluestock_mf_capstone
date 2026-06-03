import pandas as pd

df = pd.read_csv(
    "data/raw/10_benchmark_indices.csv"
)

df["date"] = pd.to_datetime(
    df["date"],
    errors="coerce"
)

df = df[df["close_value"] > 0]

df = df.drop_duplicates()

df.to_csv(
    "data/processed/benchmark_indices_clean.csv",
    index=False
)

print("Benchmark indices cleaned successfully")