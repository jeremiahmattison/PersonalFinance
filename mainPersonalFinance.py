import AccountingSystem
import BudgetExpenseTracker
import LoanCalculatorProject

class PersonalFinance:
    def __init__(self):
        self.accounting_system = AccountingSystem.ACCOUNTINGSYSTEM()
        self.budget_expense_tracker = BudgetExpenseTracker.BUDGETEXPENSETRACKER()
        self.loan_calculator = LoanCalculatorProject.LOANCALCULATOR()

    def display_menu(self):
        while True:
            print("\nMain Menu:")
            print("1. Accounting System")
            print("2. Budget/Expense Tracker")
            print("3. Loan Calculator")
            print("4. Exit")

            try:
                choice = int(input("Enter your choice number: "))
            except ValueError:
                print("Invalid choice. Please enter a number.")
                continue

            if choice == 1:
                self.accounting_menu()
            elif choice == 2:
                self.budget_menu()
            elif choice == 3:
                self.loan_calculator.begin()
            elif choice == 4:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")

    def accounting_menu(self):
        while True:
            print("\nAccounting System Menu:")
            print("1. Create Account")
            print("2. Record Transaction")
            print("3. View Balances")
            print("4. Back to Main Menu")

            try:
                choice = int(input("Enter your choice number: "))
            except ValueError:
                print("Invalid choice. Please enter a number.")
                continue

            if choice == 1:
                self.accounting_system.create_account()
            elif choice == 2:
                self.accounting_system.record_transaction()
            elif choice == 3:
                self.accounting_system.view_balances()
            elif choice == 4:
                break
            else:
                print("Invalid choice. Please try again.")

    def budget_menu(self):
        while True:
            print("\nBudget/Expense Tracker Menu:")
            print("1. Add Expense")
            print("2. View Total Expense")
            print("3. View Expense By Category")
            print("4. Back to Main Menu")

            try:
                choice = int(input("Enter your choice number: "))
            except ValueError:
                print("Invalid choice. Please enter a number.")
                continue

            if choice == 1:
                self.budget_expense_tracker.add_expense()
            elif choice == 2:
                self.budget_expense_tracker.view_total_expenses()
            elif choice == 3:
                self.budget_expense_tracker.view_expense_by_category()
            elif choice == 4:
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    pf = PersonalFinance()
    pf.display_menu()