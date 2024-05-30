#LoanCalculator
class LOANCALCULATOR:
    # define the loan calculator function

    def calculate_loan(self, principal, annual_interest_rate, years):
        monthly_interest_rate = annual_interest_rate / 12 / 100

    # the amount of payments
        amt_payments = years * 12

    # the monthly payment using the formula for a fixed-rate loan. This is the formula to pay off a loan over a certain perioud of time
        monthly_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate) ** amt_payments) / ((1 + monthly_interest_rate) ** amt_payments - 1)

    # total payment 
        total_payment = monthly_payment * amt_payments

    # total interest
        total_interest = total_payment - principal
        return total_payment, total_interest, monthly_payment

    # define the main function to interact with the user
    def begin(self): 
    # next: setup to ask for user for input 
        principal = float(input("Enter the loan amount: $"))
        annual_interest_rate = float(input("Enter the annual interest rate: "))
        years = int (input("Enter the number of years for the loan: "))

        monthly_payment, total_payment, total_interest = self.calculate_loan(principal, annual_interest_rate, years)

    # display results
        print("\nLoan Details:")
        print(f"Princial Amount: ${principal}")
        print(f"Annual Interest Rate: {annual_interest_rate}%")
        print(f"Number of Years: {years}")
        print("\nMonthly Payment:", round(monthly_payment, 2))
        print("Total Payment:", round(total_payment, 2))
        print("Total Interest:", round(total_interest, 2))
