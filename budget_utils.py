from collections import defaultdict

def group_by_category(transactions):
    grouped = defaultdict(float)
    for t in transactions:
        category = t["category"]
        amount = float(t["amount"])
        grouped[category] += amount
    return grouped