# Data Analyst Portfolio — Five Mini Projects

Five independent, beginner-friendly Python projects suitable for a GitHub portfolio. Each contains a **synthetic dataset**, a reproducible analysis script, and automatically generated chart and summary.

| Project | Business question | Core method |
|---|---|---|
| [Customer Churn](01-customer-churn/) | Who is likely to cancel? | Cohort rates + logistic regression |
| [Sales Forecast](02-sales-forecast/) | What could sales look like next quarter? | Linear trend + seasonal indicators |
| [Retail Seasonality](03-retail-seasonality/) | When are sales highest? | Grouped averages |
| [Fraud Patterns](04-fraud-patterns/) | Which transactions merit review? | Transparent rule-based anomaly flags |
| [A/B Testing](05-ab-testing/) | Does landing page B convert better? | Two-proportion z-test |

## Quick start

```bash
python -m pip install -r requirements.txt
python 01-customer-churn/analyze.py
python 02-sales-forecast/analyze.py
python 03-retail-seasonality/analyze.py
python 04-fraud-patterns/analyze.py
python 05-ab-testing/analyze.py
```

Each project saves charts, tabular outputs where applicable, and a summary in its `output/` directory. Those outputs are included in this repository so reviewers can preview results without running code.


**All records are simulated.** They are designed for demonstration only; no real-world prediction performance or validated business impact is claimed. The fraud project **does not identify confirmed fraud**. The forecast uses a simplified model and a small synthetic time series; the A/B test assumes randomized independent visitors.

