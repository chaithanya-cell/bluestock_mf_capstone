import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine(
    "sqlite:///data/db/bluestock_mf.db"
)

datasets = {

    "dim_fund":
    "data/processed/fund_master_clean.csv",

    "fact_nav":
    "data/processed/nav_history_clean.csv",

    "fact_aum":
    "data/processed/aum_by_fund_house_clean.csv",

    "fact_sip":
    "data/processed/monthly_sip_inflows_clean.csv",

    "fact_category_inflows":
    "data/processed/category_inflows_clean.csv",

    "fact_folio":
    "data/processed/industry_folio_count_clean.csv",

    "fact_performance":
    "data/processed/scheme_performance_clean.csv",

    "fact_transactions":
    "data/processed/investor_transactions_clean.csv",

    "fact_portfolio":
    "data/processed/portfolio_holdings_clean.csv",

    "fact_benchmark":
    "data/processed/benchmark_indices_clean.csv"
}

for table_name, file_path in datasets.items():

    print(f"Loading {table_name}...")

    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(
        f"{table_name} loaded successfully"
    )

print("\nDatabase creation completed.")