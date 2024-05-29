def calculate_savings(monthly_income, monthly_expenses):
    savings = monthly_income - monthly_expenses
    return savings


def calculate_monthly_budget(monthly_income, monthly_expenses):
    budget = {
        "income": monthly_income,
        "expenses": monthly_expenses,
        "savings": calculate_savings(monthly_income, monthly_expenses)
    }
    return budget


def main():
    try:
        monthly_income = float(input("Enter your monthly income: $"))
        monthly_expenses = float(input("Enter your monthly expenses: $"))

        monthly_budget = calculate_monthly_budget(monthly_income, monthly_expenses)

        print("\nYour monthly budget details:")
        print("Income: ${}".format(monthly_budget['income']))
        print("Expenses: ${}".format(monthly_budget['expenses']))
        print("Savings: ${}".format(monthly_budget['savings']))

    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()
