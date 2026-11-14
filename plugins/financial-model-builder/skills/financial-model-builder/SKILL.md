---
name: financial-model-builder
description: >
  Build professional Excel financial models with structured inputs, calculated outputs, colour-coded
  formatting, and amortisation or scenario tables. Use this skill whenever the user asks to build,
  create, or improve any Excel or spreadsheet model — including loan and mortgage calculators,
  breakeven analysis, AI cost models, headcount (full-time equivalent) models, comparators, budget
  tools, or any model with inputs and outputs. Also use it when the user uploads a spreadsheet and
  wants it enhanced, restructured or extended with new logic, even when phrased as "build me a simple
  model" or "can you make a spreadsheet for X".
---

# Financial Model Builder

Build clean, error-free spreadsheet models that business users can actually use.

This skill needs no profile file. Everything it needs comes from the user's request. If the purpose,
the inputs or the currency are unclear, ask before building. Never guess a rate, price or amount.

## Step 1: Understand the model

Before building, confirm:
1. **Purpose**: what decision does this model support? (loan comparison, headcount planning, breakeven…)
2. **Inputs**: what does the user control? (rates, prices, quantities, time periods)
3. **Outputs**: what do they want to see? (monthly payment, total cost, savings, curves)
4. **Complexity**: one sheet or several? Scenarios? Charts?
5. **Region and currency**: number formats, decimal separator and financial conventions.

Suggest 2–3 extra outputs that would add value if the user has not thought of them.

## Step 2: Check the tools

- Use `openpyxl` in Python (`pip install openpyxl` if missing).
- If an `xlsx` skill is available in this session, read it before writing code and follow its rules.
- To recalculate formulas and find errors, use the bundled script
  `${CLAUDE_PLUGIN_ROOT}/skills/financial-model-builder/scripts/recalc_check.py`. It needs LibreOffice
  (`soffice`) on the machine. If LibreOffice is missing, say so and tell the user the error check did not run.

## Step 3: Design the structure

### Standard sheet layout
- **Inputs** sheet (or section): blue input cells, clear labels, units shown.
- **Calculations** sheet (or section): formula-driven, never hard-coded constants.
- **Summary** sheet: key results, highlighted, with conditional formatting.
- **Schedule**: for time series (loans, forecasts), one row per period (for example 360 rows for a 30-year monthly loan).
- **Scenarios**: if requested, a sensitivity table (for example interest rate ±1 and ±2 points).

### Colour code
- Blue: input cells (the user edits these)
- Green: positive outputs and savings
- Red: costs, payments, negative flows
- Yellow: interest or rate figures
- Dark navy header rows: section dividers

## Step 4: Build the model

- **No hard-coded constants** in formula cells. Every value points to a named cell or input row.
- **Named ranges** for key inputs (for example `LoanAmount`, `FixedRate`, `TermMonths`).
- **IFERROR** around divisions and lookups.
- **Freeze the top rows** and add a filter on table headers.
- **Recalculate and check**: `python3 recalc_check.py <file.xlsx>`. It prints the formula count and every error cell.
- **Zero formula errors** before delivering. Fix every #REF!, #DIV/0!, #NAME? and #VALUE!.

## Step 5: Document and deliver

- Add an "Instructions" tab that explains the inputs and the colour code.
- Tell the user the formula count and the error count.
- For a known model type, show the key formula (for example the fixed-payment loan formula
  `P × i(1+i)^n / [(1+i)^n − 1]`).
- This is a calculation tool, not financial advice. Say so when the model supports a money decision.

## Model templates

### Loan or mortgage
- Inputs: price, deposit, rate(s), term, costs, discounts.
- Key formula: `=PMT(rate/12, months, -principal)`
- Schedule: one row per month (Month, Payment, Interest, Principal, Balance, Costs, Cash flow).
- Outputs: total paid, total interest, loan-to-value ratio, maximum affordable loan, affordability check.

### Loan comparator (several lenders)
- Inputs sheet: one column per offer.
- One sheet per offer with its full schedule.
- Summary: present value of the total cost per offer, ranking, best-option flag.

### AI or automation breakeven
- Inputs: team size, average cost per full-time person, tool subscription, usage cost per person, efficiency gain.
- Curves: salary savings (steps, because people are whole numbers) against AI costs (continuous).
- Output: breakeven adoption rate, net gain by scenario, and a sensitivity tab for higher usage when work gets cheaper.

### Bid or project cost model
- Inputs: roles, day rates, days, travel, expenses.
- Output: total price, margin, sensitivity to how many days are billable.
