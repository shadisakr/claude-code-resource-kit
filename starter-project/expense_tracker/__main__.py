import sys

from . import core, storage

USAGE = """Usage:
  python -m expense_tracker add AMOUNT CATEGORY [NOTE]
  python -m expense_tracker list
  python -m expense_tracker summary YYYY-MM
"""


def main(argv):
    if not argv:
        print(USAGE)
        return 1

    cmd, args = argv[0], argv[1:]
    expenses = storage.load()

    if cmd == "add" and len(args) >= 2:
        note = " ".join(args[2:])
        expense = core.make_expense(args[0], args[1], note)
        expenses.append(expense)
        storage.save(expenses)
        print(f"Added {core.format_cents(expense['amount'])} to {expense['category']}")
        return 0

    if cmd == "list":
        for e in expenses:
            print(f"{e['date']}  {core.format_cents(e['amount']):>10}  {e['category']:<12} {e['note']}")
        return 0

    if cmd == "summary" and len(args) == 1:
        totals, grand = core.summarize(expenses, args[0])
        for cat, cents in sorted(totals.items()):
            print(f"{cat:<12} {core.format_cents(cents):>10}")
        print(f"{'TOTAL':<12} {core.format_cents(grand):>10}")
        return 0

    print(USAGE)
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
