import csv
from datetime import datetime

class Expense:
    def __init__(self, category, amount, date):
        self.category = category
        self.amount = amount
        self.date = date

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, amount, date_str):
        date = datetime.strptime(date_str, '%Y-%m-%d')
        expense = Expense(category, amount, date)
        self.expenses.append(expense)
        self.save_expenses()

    def get_total_spending(self):
        return sum(expense.amount for expense in self.expenses)

    def get_total_savings(self, income):
        return income - self.get_total_spending()

    def get_spending_by_category(self):
        category_spending = {}
        for expense in self.expenses:
            if expense.category in category_spending:
                category_spending[expense.category] += expense.amount
            else:
                category_spending[expense.category] = expense.amount
        return category_spending

    def get_monthly_report(self, year, month):
        monthly_expenses = []
        for expense in self.expenses:
            if expense.date.year == year and expense.date.month == month:
                monthly_expenses.append(expense)
        total_spending = sum(expense.amount for expense in monthly_expenses)
        return {
            'month': month,
            'year': year,
            'expenses': monthly_expenses,
            'total_spending': total_spending,
        }

    def get_annual_report(self, year):
        annual_expenses = []
        for expense in self.expenses:
            if expense.date.year == year:
                annual_expenses.append(expense)
        total_spending = sum(expense.amount for expense in annual_expenses)
        return {
            'year': year,
            'expenses': annual_expenses,
            'total_spending': total_spending,
        }

    def suggest_budgets(self):
        category_spending = self.get_spending_by_category()
        total_spending = self.get_total_spending()
        budgets = {}
        for category, spending in category_spending.items():
            budget = spending / total_spending * 100
            budgets[category] = budget
        return budgets

    def save_expenses(self):
        with open('expenses.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for expense in self.expenses:
                writer.writerow([expense.category, expense.amount, expense.date.strftime('%Y-%m-%d')])

    def load_expenses(self):
            with open('expenses.csv', newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    category, amount, date_str = row
                    amount = float(amount)
                    date = datetime.strptime(date_str, '%Y-%m-%d')
                    expense = Expense(category, amount, date)


def main():
    tracker = ExpenseTracker()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Category Spending")
        print("4. View Overall Spending")
        print("5. View Total Savings")
        print("6. Generate Monthly Report")
        print("7. Generate Annual Report")
        print("8. Suggest Budget")
        print("9. Save Expenses to File")
        print("10. Load Expenses from File")
        print("11. Exit")
        choice = input("Enter your choice (1-11): ")
        if choice == "1":
            category = input("Enter the category of the expense: ")
            amount = float(input("Enter the amount spent: "))
            date_str = input("Enter the date (YYYY-MM-DD): ")
            tracker.add_expense(category, amount, date_str)
        elif choice == "2":
            tracker.load_expenses()
        elif choice == "3":
            tracker.get_spending_by_category()
        elif choice == "4":
            tracker.get_total_spending()
        elif choice == "5":
            income = float(input("Enter your income: "))
            tracker.get_total_savings(income)
        elif choice == "6":
            month = int(input("Enter the month (1-12): "))
            year = int(input("Enter the year: "))
            tracker.get_monthly_report(month, year)
        elif choice == "7":
            year = int(input("Enter the year: "))
            tracker.get_annual_report(year)
        elif choice == "8":
            tracker.suggest_budgets()
        elif choice == "9":
            filename = input("Enter the filename to save expenses: ")
            tracker.save_expenses(filename)
        elif choice == "10":
            filename = input("Enter the filename to load expenses from: ")
            tracker.load_expenses(filename)
        elif choice == "11":
            break
        else:
            print("Invalid choice! Please try again.")

main()
