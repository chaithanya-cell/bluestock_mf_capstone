
 01_fund_master.csv

Column             Data Type       Description                                                amfi_code           Integer    Unique AMFI scheme identifier                              fund_house          Text       Mutual Fund Asset Management Company (AMC)                 scheme_name         Text       Name of the mutual fund scheme                            category            Text       Broad category of the scheme (Equity, Debt, Hybrid)        sub_category        Text       Specific category such as Large Cap, Small Cap, Gilt, etc. plan                Text       Plan type (Regular or Direct)                             launch_date         Date       Date on which the scheme was launched                      benchmark           Text       Benchmark index used for performance comparison expense_ratio_pct   Float      Annual expense ratio charged by the fund (%)        exit_load_pct       Float      Exit load charged on redemption (%)                  min_sip_amount      Integer    Minimum SIP investment amount (INR)                        
min_lumpsum_amount  Integer    Minimum lump sum investment amount (INR)                   
fund_manager        Text       Name of the fund manager                                   
risk_category       Text       Risk classification of the scheme                          sebi_category_code  Text       SEBI classification code for the scheme                    


02_nav_history.csv

Column	        Type	            Description
amfi_code	   Integer	      Unique AMFI scheme code
date	        Date	      NAV date
nav	            Float	      Net Asset Value of the scheme


03_aum_by_fund_house.csv

 Column       Data Type  Description                           
 date         Date       Reporting date                        
 fund_house   Text       Name of the mutual fund company (AMC) 
 aum_lakh     Float      Total AUM in lakh crore rupees        
 aum_crore    Float      Total AUM in crore rupees             
 num_schemes  Integer    Number of schemes managed by the AMC  


04_monthly_sip_inflows.csv

 Column                      Data Type                   Description 
 month                       Date/Text        Month of observation (YYYY-MM) 
 sip_inflow_crore            Integer     Total SIP inflow collected during the month (₹ crore) 
 active_sip_accounts_crore   Float          Number of active SIP accounts (crore) 
 new_sip_accounts_lakh       Float         New SIP accounts registered during the month (lakh) 
 sip_aum_lakh_crore          Float          SIP Assets Under Management (lakh crore) 
 yoy_growth_pct              Float          Year-over-Year growth percentage of SIP inflows 


05_category_inflows.csv

 Column                 Data Type               Description 
 month                  Date/Text           Month of inflow data (YYYY-MM) 
 category               Text               Mutual fund category 
 net_inflow_crore       Float               Net inflow received by the category (₹ crore) 


06_industry_folio_count.csv

 Column                 Data Type                       Description 
 month                  Date/Text                Reporting month (YYYY-MM) 
 total_folios_crore     Float                    Total mutual fund folios in crore 
 equity_folios_crore    Float                    Equity mutual fund folios in crore 
 debt_folios_crore      Float                    Debt mutual fund folios in crore 
 hybrid_folios_crore    Float                    Hybrid mutual fund folios in crore 
 others_folios_crore    Float                    Folios belonging to other categories in crore 


07_scheme_performance.csv

Column	            Data Type	            Description
amfi_code	        Integer	        Unique AMFI scheme identifier
scheme_name	        Text	        Mutual fund scheme name
fund_house	        Text	        Asset Management Company (AMC)
category	        Text	        Fund category
plan	            Text	        Direct or Regular plan
return_1yr_pct	    Float	        One-year return percentage
return_3yr_pct	    Float	        Three-year annualized return percentage
return_5yr_pct	    Float	        Five-year annualized return percentage
benchmark_3yr_pct	Float	        Three-year benchmark return percentage
alpha	            Float	        Excess return over benchmark
beta	            Float	        Measure of market-related risk
sharpe_ratio	    Float	        Risk-adjusted return metric
sortino_ratio	    Float	        Downside risk-adjusted return metric
std_dev_ann_pct 	Float	        Annualized standard deviation (%)
max_drawdown_pct	Float	        Maximum decline from peak value (%)
aum_crore	        Float	        Assets Under Management (₹ crore)
expense_ratio_pct	Float	        Annual expense ratio (%)
morningstar_rating	Integer	        Morningstar rating (1–5 stars)
risk_grade	        Text	        Risk classification of the scheme


08_investor_transactions.csv

Column	            Data Type	            Description
investor_id	        Text	        Unique identifier for an investor
transaction_date	Date	        Date of the transaction
amfi_code	        Integer	        Unique AMFI scheme identifier
transaction_type	Text	        Type of transaction (SIP, Lumpsum, Redemption)
amount_inr	        Float	        Transaction amount in Indian Rupees
state	            Text	        State of the investor
city	            Text	        City of the investor
city_tier	        Text	        Investor city classification (T30/B30)
age_group	        Text	        Age group category of the investor
gender	            Text	        Gender of the investor
annual_income_lakh	Float	        Annual income of the investor (₹ lakh)
payment_mode	    Text	        Mode of payment (UPI, Net Banking, Debit Card, etc.)
kyc_status	        Text	        KYC verification status of the investor


09_portfolio_holdings.csv

Column	            Data Type	            Description
amfi_code	        Integer	            Unique AMFI scheme identifier
stock_symbol	    Text	            Stock ticker symbol
stock_name	        Text	            Name of the company/security held
sector	            Text	            Industry sector of the holding
weight_pct	        Float	            Percentage weight of the holding in the portfolio
market_value_cr	    Float	            Market value of the holding in crore rupees
current_price_inr	Float	            Current market price of the security in INR
portfolio_date	    Date	            Portfolio disclosure date


10_benchmark_indices.csv

Column	            Data Type	            Description
date	            Date	            Trading date
index_name	        Text	            Name of benchmark index
close_value     	Float	            Closing value of the benchmark index