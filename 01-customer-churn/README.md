# Customer Churn Analysis

> **Portfolio level:** beginner / entry-level analyst · **Language:** Python · **Dataset:** synthetic

## 1. Business problem

A subscription company wants to understand customer cancellation risk and prioritize retention outreach.

**Question:** Which customers appear more likely to churn, and does customer tenure relate to cancellations?

## 2. Dataset and columns

Data file: [`data/customers.csv`](data/customers.csv)

| Field | Meaning |
|---|---|
| `customer_id` | Synthetic customer identifier; excluded from modeling |
| `tenure_months` | Months since the customer joined |
| `monthly_fee_usd` | Monthly subscription fee in USD |
| `support_tickets` | Count of customer support tickets |
| `annual_contract` | 1 for annual plan; 0 otherwise |
| `churned` | Target: 1 left; 0 remained |

All values are simulated for teaching and portfolio use.

## 3. Tools and skills demonstrated

- **Python / Pandas:** loading, transforming, grouping and summarizing data
- **Matplotlib:** communicating findings visually
- **Scikit-learn:** simple predictive modeling or evaluation
- **GitHub documentation:** reproducible analysis, business explanation, conclusions, limitations

## 4. Methodology — step by step

1. Load customers with `pd.read_csv` and calculate the mean of `churned` to estimate overall churn.
2. Bin tenure into four groups using `pd.cut`; calculate each group's churn rate with `groupby().mean()`.
3. Split observations into training (75%) and test (25%) sets with stratification to preserve churn class proportions.
4. Fit a **logistic regression** using tenure, fee, ticket count, and contract indicator. These are illustrative predictors, not proof of causality.
5. Evaluate ranking performance on the untouched test set using **ROC AUC**, then export a bar chart and text summary.

## 5. Results (from the included script)

- **Overall churn:** 13.3% of synthetic customers.
- **1–12 months tenure:** 27.0% churn; **37–60 months:** 7.8%.
- **Test ROC AUC:** 0.781. AUC measures how well the model ranks churners above non-churners (0.5 is random ranking; 1.0 is perfect).

## 6. What the results mean for the business

Newer customers have the highest observed churn rate in this example. A sensible business follow-up is to review onboarding and early-life support. This analysis is **associational**, not evidence that tenure causes churn.

## 7. Limitations and responsible interpretation

Small artificial sample, no temporal holdout, no calibration or cost-sensitive threshold selection. ROC AUC is not the same as accuracy. Real deployment would require recent real data, leakage review, fairness checks and monitoring.

## 8. Files to explore

- `analyze.py`: complete readable script; start here for the analysis steps.
- `data/`: source CSV; opening this in Excel is also a useful way to inspect the inputs.
- `output/summary.txt`: key computed outcomes.
- `output/*.png`: visual chart for a recruiter to preview.
- Other `output/*.csv` files, when available, contain actionable exports.

## How to run

From the portfolio root, create an environment and install dependencies:

```bash
python -m venv .venv
# macOS/Linux:
source .venv/bin/activate
# Windows PowerShell:
# .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Then run this specific project from the portfolio root:

```bash
python 01-customer-churn/analyze.py
```

The script reads the committed CSV in `data/` and writes charts, summaries, and any export files to `output/`. Existing outputs can be reproduced by rerunning the script.

**Data provenance:** educational **synthetic** data. These results do not describe any actual customers, sales, fraud cases, or controlled experiments. No proprietary or personal data are used.


## 9. How to explain this project in an interview

“I analyzed subscription churn using Pandas and logistic regression. I grouped customers by tenure, compared churn rates, and evaluated a model on a held-out test set. I would investigate onboarding because newer customers showed higher churn.”

## 10. Optional next improvement (not needed for this version)

Add one additional chart or a short SQL query that recreates a core grouped metric. The existing project is deliberately small, complete and reproducible.
