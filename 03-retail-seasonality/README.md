# Retail Sales Seasonality

> **Portfolio level:** beginner / entry-level analyst · **Language:** Python · **Dataset:** synthetic

## 1. Business problem

A retailer wants to recognize recurring demand peaks and adjust scheduling and promotions.

**Question:** Which months and weekdays tend to generate higher average daily sales?

## 2. Dataset and columns

Data file: [`data/daily_sales.csv`](data/daily_sales.csv)

| Field | Meaning |
|---|---|
| `date` | Date of sale aggregation |
| `sales_usd` | Synthetic total sales for that day |

All values are simulated for teaching and portfolio use.

## 3. Tools and skills demonstrated

- **Python / Pandas:** loading, transforming, grouping and summarizing data
- **Matplotlib:** communicating findings visually
- **Descriptive statistics:** hypothesis testing or analytic logic
- **GitHub documentation:** reproducible analysis, business explanation, conclusions, limitations

## 4. Methodology — step by step

1. Read daily sales with the date parsed into a datetime column.
2. Extract numeric **calendar month** and **weekday name** from the date.
3. Group by month and calculate the **average daily sales**, ensuring months of different lengths are comparable.
4. Group by weekday to identify operational peaks and reorder days Monday–Sunday for readability.
5. Plot the monthly averages and write a short results summary.

## 5. Results (from the included script)

- **Highest average month:** December, **$2,001 per day**.
- **Highest average weekday:** Saturday, **$1,616 per day**.

## 6. What the results mean for the business

Synthetic demand is concentrated around December and Saturdays. A retailer could test additional weekend staffing and holiday inventory buffers, then verify the pattern against real multiple-year transactions.

## 7. Limitations and responsible interpretation

An average by calendar month is a descriptive pattern, **not a seasonality forecast**. Trend, outliers, unequal day counts and special events may affect averages; no formal decomposition or significance testing is done.

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
python 03-retail-seasonality/analyze.py
```

The script reads the committed CSV in `data/` and writes charts, summaries, and any export files to `output/`. Existing outputs can be reproduced by rerunning the script.

**Data provenance:** educational **synthetic** data. These results do not describe any actual customers, sales, fraud cases, or controlled experiments. No proprietary or personal data are used.


## 9. How to explain this project in an interview

“I used Pandas datetime operations and grouping to reveal monthly and weekday sales patterns. The result highlights potential staffing and inventory adjustments, while recognizing that descriptive patterns need validation.”

## 10. Optional next improvement (not needed for this version)

Add one additional chart or a short SQL query that recreates a core grouped metric. The existing project is deliberately small, complete and reproducible.
