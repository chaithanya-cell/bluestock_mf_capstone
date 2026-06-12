#(Mutual Fund Recommendation Engine

#This script recommends the top mutual fund schemes based on the user's selected risk appetite.

#The recommendation is generated using Sharpe Ratio rankings within the selected risk category.

import pandas as pd

# Load data
scheme = pd.read_csv(
    "../data/processed/scheme_performance_clean.csv"
)

print("\nAvailable Risk Levels:")
print(
    scheme['risk_grade']
    .dropna()
    .unique()
)

risk = input(
    "\nEnter Risk Level: "
)

# Filter funds
result = scheme[
    scheme['risk_grade'] == risk
]

# Sort by Sharpe Ratio
result = result.sort_values(
    'sharpe_ratio',
    ascending=False
)

# Top 3 recommendations
top3 = result[
    [
        'scheme_name',
        'risk_grade',
        'sharpe_ratio'
    ]
].head(3)

print("\nTop 3 Recommended Funds:\n")
print(top3)

# Save report
top3.to_csv(
    "top3_recommendations.csv",
    index=False
)

print("\nRecommendations saved!")