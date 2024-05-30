class BUDGETEXPENSETRACKER:# dictionary to store expenses
    def __init__(self):
        self.expenses = {}

    def add_expense(self):
        try:
            amount = float(input("\nEnter expense amount: "))
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
            return

        category = input("Enter expense category: ")

        if category in self.expenses:
            self.expenses[category].append(amount)
        else:
            self.expenses[category] = [amount]

        print("Expense successfully added.")

    def view_total_expenses(self):
        total = sum(sum(category_expenses) for category_expenses in self.expenses.values())
        print(f"\nTotal Expenses: ${total:.2f}")

    def view_expense_by_category(self):
        for category, category_expenses in self.expenses.items():
            print(f"\nExpenses for {category}:")
            for expense in category_expenses:
                print(f"- ${expense:.2f}")
