# Answer key (spoilers)

1. **Amounts lose a cent** (`core.parse_amount`). `float("19.99") * 100` is `1998.9999...`, and `int()` cuts it to `1998`. Fix: parse with `decimal.Decimal` and round, or split on the dot.

2. **Monthly summary ignores the year** (`core.in_month`). It compares only the month digits, so `summary 2026-11` also counts November 2025. Fix: compare `expense["date"][:7] == month`.

3. **Grand total is wrong** (`core.summarize`). The loop does `grand = totals[cat]` instead of `+=`, so the total is just the last category. Fix: `grand = sum(totals.values())`.

4. **Crash on an empty data file** (`storage.load`). If `expenses.json` exists but is empty, `json.load` raises `JSONDecodeError`. Fix: return `[]` when the file is empty, and decide what to do with a corrupt file (warn, don't silently overwrite the user's data).

Bonus finding if Claude spots it: categories are case-sensitive, so `Food` and `food` are totalled separately.
