import pandas as pd
from pathlib import Path

for file in Path("data/raw").glob("*.csv"):
    df = pd.read_csv(file)

    print(file.name)
    print("Duplicates:", df.duplicated().sum())
    print("-" * 30)