# Data Analyst Portfolio — Five Beginner-Friendly Case Studies

**Goal:** showcase foundational data-analysis skills with short, reproducible projects and clear business explanations. Each project includes a dataset, a runnable Python analysis, an image, outcomes, limitations, and an interview-ready summary.

> **Transparency:** All datasets are **synthetic**, and analyses were created for portfolio demonstration. Results do not represent verified business outcomes or paid professional work.

## Start here

| Project | Business question | Main methods | Result snapshot |
|---|---|---|---|
| [01 Churn](01-customer-churn/) | Which customers are more likely to leave? | Tenure cohorts, logistic regression, ROC AUC | 13.3% churn; AUC 0.781 |
| [02 Forecast](02-sales-forecast/) | How much might next-month revenue be? | Time-ordered holdout, linear regression, MAE | Holdout MAE $475.49 |
| [03 Seasonality](03-retail-seasonality/) | When do sales peak? | Date parsing, monthly/weekday averages | December and Saturday peaks |
| [04 Fraud patterns](04-fraud-patterns/) | Which payments merit review? | Transparent rules, anomaly triage | 52/1,500 flagged; not confirmed fraud |
| [05 A/B testing](05-ab-testing/) | Did version B improve conversion? | Two-proportion z-test | +2.02 points; p = 0.0382 |

## How to reproduce all analyses

Requires **Python 3.10+**. From this directory:

```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
python 01-customer-churn/analyze.py
python 02-sales-forecast/analyze.py
python 03-retail-seasonality/analyze.py
python 04-fraud-patterns/analyze.py
python 05-ab-testing/analyze.py
```

Each script uses file paths relative to itself, so commands work from the portfolio root. Outputs are already included for browser preview.

## How to navigate each project

1. Open that project's `README.md` for the business context, dataset definitions, methodology and interpretation.
2. Preview the chart in `output/` and confirm exact metrics in `output/summary.txt`.
3. Read `analyze.py`, which runs the full analysis with local data.
4. Re-run the command above to demonstrate reproducibility.

## Common interview framework

Describe each project in this order: **business problem → dataset → cleaning/analysis → result → recommended next step → limitation**. Avoid presenting these simulations as actual client experience.

## GitHub publishing

**Option A — one repository (recommended to start):** create a public repository named `data-analyst-portfolio`, upload all extracted files including this README, then commit. The relative README links work on GitHub.

**Option B — five separate repositories:** upload the content of each numbered project folder to a repository with a descriptive name; copy `requirements.txt` into each repo. Link all five from your GitHub profile README.

Do not upload `.venv/`, credentials or personal information. This package uses no secrets.

## Dataset and methodology cautions

- These are intentionally minimal **educational** models, not deployed production systems.
- Churn AUC is ranking quality, **not** accuracy.
- A forecast is an estimate with error, not a guarantee.
- Seasonal averages alone do not establish a forecasting model.
- Unusual payment activity is **not** confirmed fraud.
- A statistically significant A/B test does not automatically justify a product rollout.
