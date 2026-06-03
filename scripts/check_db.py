import sqlite3

conn = sqlite3.connect(
    "data/db/bluestock_mf.db"
)

cur = conn.cursor()

cur.execute(
    "SELECT COUNT(*) FROM dim_fund"
)

print(cur.fetchone())

conn.close()