import json
import os
from datetime import datetime
from budget_utils import group_by_category

DATA_FILE = "transactions.json"

# Transaction class
class Transaction:
    def __init__(self, date, category, amount):
        self.date = date
        self.category = category
        self.amount = amount

    def to_dict(self):
        return {
            "date": self.date,
            "category": self.category,
            "amount": self.amount
        }

# Load data
def load_transactions():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

# Save data
def save_transactions(transactions):
    with open(DATA_FILE, "w") as f:
        json.dump(transactions, f, indent=4)

# Add a transaction
def add_transaction():
    date = input("Enter date following this format- (YYYY-MM-DD) or leave blank for today: ")
    if not date:
        date = datetime.today().strftime("%Y-%m-%d")
    category = input("Enter category (e.g., food, transport): ")
    amount = float(input("Enter amount: "))

    t = Transaction(date, category, amount)
    transactions.append(t.to_dict())
    save_transactions(transactions)
    print("Transaction added!\n")

# View all transactions
def view_transactions():
    if not transactions:
        print("No transactions recorded.\n")
        return
    for t in transactions:
        print(f"{t['date']} | {t['category']} | ${t['amount']:.2f}")
    print()

# View totals by category
def view_totals_by_category():
    totals = group_by_category(transactions)
    print("\nTotal by category:")
    for category, total in totals.items():
        print(f"{category}: ${total:.2f}")
    print()

# Load existing data
transactions = load_transactions()

# Menu
while True:
    print("=== Personal Budget Tracker ===")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. View Totals by Category")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_transaction()
    elif choice == "2":
        view_transactions()
    elif choice == "3":
        view_totals_by_category()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option.\n")