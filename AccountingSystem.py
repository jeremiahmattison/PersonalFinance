class ACCOUNTINGSYSTEM:
    
    # also create a dictionary to store the account names and balances
    def __init__(self):
        self.accounts = {}

    # create a function to create a new account
    def create_account(self):
        account_name = input("Enter account name: ")
        initial_balance = float(input("Enter initial balance: "))
        self.accounts[account_name] = initial_balance

    # create a function to record a transaction
    def record_transaction(self):
        debit_account = input("Enter existing debit account name: ")
        credit_account = input("Enter existing credit account name: ")
        amount = float(input("Enter transaction amount: "))
        if debit_account not in self.accounts:
            print("Error: No debit account found.")
            return
        if credit_account not in self.accounts:
            print("Error: No credit account found")
            return

        self.accounts[debit_account] -= amount
        self.accounts[credit_account] += amount
        
    # create a function to view the account balances
    def view_balances(self):
        for account, balance in self.accounts.items():
            print(f"{account}: {balance}")

    

