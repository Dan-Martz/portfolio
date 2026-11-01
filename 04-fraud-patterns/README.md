# Transaction Anomaly Screening

> **Portfolio level:** beginner / entry-level analyst · **Language:** Python · **Dataset:** synthetic

## 1. Business problem

A payments operations team needs an explainable way to shortlist unusual transactions for manual review.

**Question:** Can basic amount and time-of-day rules identify a manageable subset of transactions worth reviewing?

## 2. Dataset and columns

Data file: [`data/transactions.csv`](data/transactions.csv)

| Field | Meaning |
|---|---|
| `transaction_id` | Synthetic transaction identifier |
| `amount_usd` | Transaction amount in USD |
| `hour` | Local transaction hour from 0 to 23 |
| `country` | Country code attached to transaction |

All values are simulated for teaching and portfolio use.

## 3. Tools and skills demonstrated

- **Python / Pandas:** loading, transforming, grouping and summarizing data
- **Matplotlib:** communicating findings visually
- **Business-rule logic:** hypothesis testing or analytic logic
- **GitHub documentation:** reproducible analysis, business explanation, conclusions, limitations

## 4. Methodology — step by step

1. Read the transaction CSV and inspect amounts and transaction-hour distribution.
2. Flag **high amount** transactions where `amount_usd >= 800`.
3. Flag **night transactions** from 00:00 through 04:59.
4. Combine rules: send a transaction for review if high amount, **or** if at night and amount exceeds $150.
5. Export every flagged row to `transactions_for_review.csv`, chart transactions by hour and report the share flagged.

## 5. Results (from the included script)

- **Transactions evaluated:** 1,500.
- **Flagged for review:** 52, or **3.5%** of the total.

## 6. What the results mean for the business

Rules reduce 1,500 rows to a much smaller review queue, which could support analyst triage. Neither the flagged count nor a rule match measures fraud prevented.

## 7. Limitations and responsible interpretation

**Do not call flagged transactions fraud.** This dataset has **no confirmed fraud labels**. No precision, recall, false-positive rate, detection rate, or financial savings can be calculated. Thresholds are hypothetical and should be tuned with domain experts and verified outcomes.

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
python 04-fraud-patterns/analyze.py
```

The script reads the committed CSV in `data/` and writes charts, summaries, and any export files to `output/`. Existing outputs can be reproduced by rerunning the script.

**Data provenance:** educational **synthetic** data. These results do not describe any actual customers, sales, fraud cases, or controlled experiments. No proprietary or personal data are used.


## 9. How to explain this project in an interview

“I built an explainable rules-based transaction screening workflow in Python. It flagged 52 of 1,500 synthetic transactions for manual review. I clearly distinguish unusual activity from confirmed fraud.”

## 10. Optional next improvement (not needed for this version)

Add one additional chart or a short SQL query that recreates a core grouped metric. The existing project is deliberately small, complete and reproducible.
