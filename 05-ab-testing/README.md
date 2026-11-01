# A/B Test: Landing Page Conversion

> **Portfolio level:** beginner / entry-level analyst · **Language:** Python · **Dataset:** synthetic

## 1. Business problem

A product team has two landing-page variants and wants to evaluate the observed difference in conversions.

**Question:** Does variation B have a different conversion rate from variation A?

## 2. Dataset and columns

Data file: [`data/experiment.csv`](data/experiment.csv)

| Field | Meaning |
|---|---|
| `visitor_id` | Synthetic visitor identifier |
| `variant` | Assigned landing page, `A` or `B` |
| `converted` | 1 converted; 0 did not |

All values are simulated for teaching and portfolio use.

## 3. Tools and skills demonstrated

- **Python / Pandas:** loading, transforming, grouping and summarizing data
- **Matplotlib:** communicating findings visually
- **SciPy:** hypothesis testing or analytic logic
- **GitHub documentation:** reproducible analysis, business explanation, conclusions, limitations

## 4. Methodology — step by step

1. Load one row per synthetic visitor and calculate conversions, sample size and conversion rate by variant.
2. Compute **absolute lift in percentage points**: rate B minus rate A.
3. Use a **two-sided two-proportion z-test** with a pooled conversion rate; the null hypothesis is that both population conversion rates are equal.
4. Compute the p-value and compare it with the predefined **0.05** threshold.
5. Plot observed conversion rates and export the findings.

## 5. Results (from the included script)

- **A:** 194 / 2,016 visitors = **9.62%**.
- **B:** 231 / 1,984 visitors = **11.64%**.
- **Absolute difference:** **+2.02 percentage points** (B − A).
- **Two-sided p-value:** **0.0382**, below the 0.05 threshold.

## 6. What the results mean for the business

There is statistical evidence of a difference **under the z-test assumptions** in the simulated sample. This alone does not prove the variation is worth shipping; team decisions should also consider effect uncertainty, cost, guardrail metrics and test integrity.

## 7. Limitations and responsible interpretation

The input is simulated. The script does not independently establish genuine random assignment, independence, pre-specified sample size, absence of peeking or real-world causal validity. Statistical significance is not the same as business significance.

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
python 05-ab-testing/analyze.py
```

The script reads the committed CSV in `data/` and writes charts, summaries, and any export files to `output/`. Existing outputs can be reproduced by rerunning the script.

**Data provenance:** educational **synthetic** data. These results do not describe any actual customers, sales, fraud cases, or controlled experiments. No proprietary or personal data are used.


## 9. How to explain this project in an interview

“I compared landing-page conversion rates, calculated a 2.02-percentage-point difference, and ran a two-proportion z-test. The synthetic test gave p = 0.0382, but I would check experiment design and business impact before launching.”

## 10. Optional next improvement (not needed for this version)

Add one additional chart or a short SQL query that recreates a core grouped metric. The existing project is deliberately small, complete and reproducible.
