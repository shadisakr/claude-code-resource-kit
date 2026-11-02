from datetime import date as _date


def parse_amount(text):
    """Turn a string like '12.50' into integer cents (1250)."""
    return int(float(text) * 100)


def format_cents(cents):
    return f"${cents // 100}.{cents % 100:02d}"


def make_expense(amount_text, category, note="", on=None):
    return {
        "date": (on or _date.today()).isoformat(),
        "amount": parse_amount(amount_text),
        "category": category,
        "note": note,
    }


def in_month(expense, month):
    """month is 'YYYY-MM'."""
    return expense["date"][5:7] == month[5:7]


def summarize(expenses, month):
    """Return {category: total_cents} for one month, plus the grand total."""
    totals = {}
    for e in expenses:
        if in_month(e, month):
            totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
    grand = 0
    for cat in totals:
        grand = totals[cat]
    return totals, grand
