import pandas as pd
from pathlib import Path

data_path = Path("data/raw")

print("Current Directory:", Path.cwd())
print("Data Path:", data_path)
print("Exists:", data_path.exists())

csv_files = list(data_path.glob("*.csv"))

for file in csv_files:

    print("="*50)
    print("File:", file.name)

    df = pd.read_csv(file)

    print("Shape:")
    print(df.shape)

    print("\nDtypes:")
    print(df.dtypes)

    print("\nHead:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())