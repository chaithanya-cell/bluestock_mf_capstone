# Capstone Project: Mutual Fund Analytics

## Project Overview

The Mutual Fund Analytics Capstone Project focuses on analyzing mutual fund performance, investor behavior, SIP trends, portfolio composition, and risk metrics using Python and Power BI.

The objective of the project is to transform raw mutual fund datasets into meaningful business insights through data cleaning, exploratory data analysis, performance evaluation, advanced analytics, and interactive dashboard development.

The project provides actionable insights for investors, analysts, and fund managers by evaluating fund performance, risk-return characteristics, investor participation patterns, and portfolio diversification. The final output includes a comprehensive Power BI dashboard, analytical reports, and a recommendation engine for mutual fund selection.

---

## Objectives

1. Analyze mutual fund industry trends and growth patterns.
2. Evaluate mutual fund performance using return and risk-adjusted metrics.
3. Assess risk-return characteristics across schemes.
4. Study investor behavior and transaction patterns.
5. Analyze SIP inflow trends and investor participation.
6. Compute advanced risk measures such as VaR and CVaR.
7. Measure portfolio concentration using HHI.
8. Develop an interactive Power BI dashboard for reporting and decision-making.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook
* Power BI
* SQLite
* Git
* GitHub

---

## Datasets

The project utilizes ten cleaned datasets:

| Dataset                         | Description                                 |
| ------------------------------- | ------------------------------------------- |
| fund_master_clean.csv           | Mutual fund metadata and scheme information |
| nav_history_clean.csv           | Historical NAV records                      |
| scheme_performance_clean.csv    | Performance metrics and return ratios       |
| investor_transactions_clean.csv | Investor transaction history                |
| portfolio_holdings_clean.csv    | Portfolio holdings and allocations          |
| benchmark_indices_clean.csv     | Benchmark index performance                 |
| monthly_sip_inflows_clean.csv   | Monthly SIP inflow statistics               |
| category_inflows_clean.csv      | Category-wise investment inflows            |
| industry_folio_count_clean.csv  | Industry folio statistics                   |
| aum_by_fund_house_clean.csv     | Assets Under Management information         |

---

## Project Structure

```text
BLUESTOCK_MF_CAPSTONE
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── EDA_Analysis.ipynb
│   ├── Performance_Analytics.ipynb
│   └── Advanced_Analytics.ipynb
│
├── scripts/
│   ├── etl.py
│   ├── recommender.py
│   ├── run_pipeline.py
│   └── data cleaning scripts
│
├── dashboard/
│   └── bluestock_mf_dashboard.pbix
│
├── reports/
│   ├── Final_Report.pdf
│   └── Bluestock_MF_Presentation.pptx
│
└── README.md
```

---

## ETL Pipeline

The project follows a structured ETL process:

```text
Raw Data
   ↓
Data Cleaning
   ↓
Data Transformation
   ↓
Feature Engineering
   ↓
Exploratory Data Analysis
   ↓
Performance & Risk Analysis
   ↓
Power BI Dashboard
```

---

## Running ETL

Execute the ETL workflow:

```bash
python scripts/etl.py
```

---

## Running the Recommender

Run the mutual fund recommendation engine:

```bash
python scripts/recommender.py
```

The recommender suggests the top-performing schemes based on the selected risk level and Sharpe Ratio ranking.

---

## Running the Full Pipeline

Execute the complete analytics workflow:

```bash
python scripts/run_pipeline.py
```

---

## Advanced Analytics Performed

### Historical VaR and CVaR

* Computed 95% Value at Risk (VaR)
* Computed Conditional Value at Risk (CVaR)

### Rolling Sharpe Ratio

* Calculated rolling 90-day Sharpe Ratios
* Visualized performance stability across schemes

### Investor Cohort Analysis

* Grouped investors by first investment year
* Analyzed investment behavior across cohorts

### SIP Continuity Analysis

* Identified investors with irregular SIP patterns
* Flagged potentially at-risk investors

### Portfolio Concentration Analysis

* Calculated Herfindahl-Hirschman Index (HHI)
* Assessed portfolio diversification levels

### Fund Recommendation Engine

* Generated scheme recommendations based on risk profile and Sharpe Ratio.

---

## Dashboard

The Power BI dashboard contains:

* Industry Overview
* Fund Performance Analysis
* Investor Analytics
* SIP & Market Trends
* Fund Details and Comparison

To open the dashboard:

```text
dashboard/bluestock_mf_dashboard.pbix
```

Open the file using Microsoft Power BI Desktop.

---

## Key Insights

* Fund 119599 exhibited the highest VaR, indicating relatively higher downside risk.
* Fund 101207 recorded the highest CVaR, suggesting larger losses during extreme market conditions.
* Fund 120505 achieved the highest HHI score, indicating greater portfolio concentration.
* Investors from the 2024 cohort contributed the highest investment volume.
* Funds with higher Sharpe Ratios generally demonstrated superior risk-adjusted performance.

---

## Author

CHAITHANYA K

Bluestock Fintech Internship

June 2026
