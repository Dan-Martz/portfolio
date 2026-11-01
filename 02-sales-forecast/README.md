# Monthly Sales Forecast

> **Portfolio level:** beginner / entry-level analyst · **Language:** Python · **Dataset:** synthetic

## 1. Business problem

A retail manager needs a reasonable estimate of short-term sales to plan staffing and inventory.

**Question:** What might revenue look like over the next three months, and how well does a simple trend-and-calendar model predict past months?

## 2. Dataset and columns

Data file: [`data/monthly_sales.csv`](data/monthly_sales.csv)

| Field | Meaning |
|---|---|
| `month` | First day of reporting month |
| `revenue_usd` | Synthetic monthly revenue in USD |

All values are simulated for teaching and portfolio use.

## 3. Tools and skills demonstrated

- **Python / Pandas:** loading, transforming, grouping and summarizing data
- **Matplotlib:** communicating findings visually
- **Scikit-learn:** simple predictive modeling or evaluation
- **GitHub documentation:** reproducible analysis, business explanation, conclusions, limitations

## 4. Methodology — step by step

1. Load 36 monthly revenue records and create a sequential month index.
2. One-hot encode calendar month (January through December) to let the model represent repeating monthly patterns.
3. Train **linear regression** on the first 30 months and evaluate on the **last six months**, rather than randomly splitting a time series.
4. Compute **mean absolute error (MAE)**: average absolute difference between predictions and observed revenue, in dollars.
5. Refit on all 36 months and predict the next three months; negative predictions are clipped to zero.
6. Save the historical-versus-predicted plot and a three-row CSV forecast.

## 5. Results (from the included script)

- **Held-out six-month MAE:** $475.49 per month.
- **Forecast January 2026:** $19,589.58.
- **Forecast February 2026:** $20,545.74.
- **Forecast March 2026:** $20,560.45.

## 6. What the results mean for the business

The forecast suggests an approximately $20K monthly revenue range under the synthetic trend and seasonality assumptions. Inventory decisions would benefit from forecasts paired with uncertainty ranges and known promotional events.

## 7. Limitations and responsible interpretation

Only 36 historical months; no holiday, promotion, pricing or economic features. Results have no prediction intervals. A single six-month holdout is a basic baseline evaluation, not robust backtesting. Forecast dates are historical relative to October 2026 because the example dataset ends in December 2025.

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
python 02-sales-forecast/analyze.py
```

The script reads the committed CSV in `data/` and writes charts, summaries, and any export files to `output/`. Existing outputs can be reproduced by rerunning the script.

**Data provenance:** educational **synthetic** data. These results do not describe any actual customers, sales, fraud cases, or controlled experiments. No proprietary or personal data are used.


## 9. How to explain this project in an interview

“I created a three-month revenue forecast using monthly seasonality indicators and a linear trend. I held out the final six months for time-based evaluation and achieved an MAE of about $475 on synthetic sales data.”

## 10. Optional next improvement (not needed for this version)

Add one additional chart or a short SQL query that recreates a core grouped metric. The existing project is deliberately small, complete and reproducible.
