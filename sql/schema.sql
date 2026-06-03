CREATE TABLE dim_fund (
amfi_code INTEGER PRIMARY KEY,
scheme_name TEXT,
fund_house TEXT,
category TEXT,
sub_category TEXT
);

CREATE TABLE dim_date (
date_id INTEGER PRIMARY KEY,
date DATE,
year INTEGER,
month INTEGER,
quarter INTEGER
);

CREATE TABLE fact_nav (
nav_id INTEGER PRIMARY KEY,
amfi_code INTEGER,
date_id INTEGER,
nav REAL,
FOREIGN KEY(amfi_code)
REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_transactions (
transaction_id INTEGER PRIMARY KEY,
amfi_code INTEGER,
amount REAL,
transaction_type TEXT
);

CREATE TABLE fact_performance (
perf_id INTEGER PRIMARY KEY,
amfi_code INTEGER,
return_1y REAL,
return_3y REAL,
return_5y REAL
);

CREATE TABLE fact_aum (
aum_id INTEGER PRIMARY KEY,
amfi_code INTEGER,
aum_crore REAL
);