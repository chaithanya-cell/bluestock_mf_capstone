-- Top 5 Funds by AUM

SELECT *
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;


-- Average NAV by Month

SELECT
strftime('%Y-%m', date),
AVG(nav)
FROM fact_nav
GROUP BY 1;


-- Funds with Expense Ratio < 1%

SELECT *
FROM dim_fund
WHERE expense_ratio < 1;


-- Total Transactions by State

SELECT
state,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;


-- Total Investment Amount by Transaction Type

SELECT
transaction_type,
SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY transaction_type;


-- Top 5 Funds by 5-Year Return

SELECT
scheme_name,
return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;


-- Average Expense Ratio by Category

SELECT
category,
AVG(expense_ratio_pct)
FROM fact_performance
GROUP BY category;


-- Number of Funds by Risk Category

SELECT
risk_category,
COUNT(*)
FROM dim_fund
GROUP BY risk_category;


-- Total Folios by Month

SELECT
month,
SUM(total_folios)
FROM industry_folio_count
GROUP BY month;


-- Benchmark Average Close Value

SELECT
AVG(close_value)
FROM benchmark_indices;