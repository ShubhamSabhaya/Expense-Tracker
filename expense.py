expenses = []

def add_expense():
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))

    expense = {
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully!\n")

def view_expenses():
    if not expenses:
        print("No expenses found.\n")
        return

    print("\nExpenses:")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['category']} - ₹{expense['amount']}")
    print()

def total_expense():
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total Expense: ₹{total}\n")

def category_report():
    categories = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    print("\nCategory Report:")
    for category, amount in categories.items():
        print(f"{category}: ₹{amount}")
    print()

while True:
    print("==== Expense Tracker ====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Category Report")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        category_report()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!\n")