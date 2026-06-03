import sqlite3

conn = sqlite3.connect(
    "data/db/bluestock_mf.db"
)

cursor = conn.cursor()

tables = [

    "dim_fund",
    "fact_nav",
    "fact_aum",
    "fact_sip",
    "fact_category_inflows",
    "fact_folio",
    "fact_performance",
    "fact_transactions",
    "fact_portfolio",
    "fact_benchmark"
]

for table in tables:

    cursor.execute(
        f"SELECT COUNT(*) FROM {table}"
    )

    count = cursor.fetchone()[0]

    print(
        f"{table}: {count} rows"
    )

conn.close()