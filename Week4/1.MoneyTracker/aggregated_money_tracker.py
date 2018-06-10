from income import Income
from expense import Expense

class AggregatedMoneyTracker:
    def __init__(self, data):
        self.incomes_list = []
        self.expenses_list = []
        self.dates_list = []
        self.expense_categories = []
        self.generate_from_data(data.parsed_data)

    def add_incomes(self, incomes, date):
        for income in incomes:
            new_income = Income(income['amount'], income['category'], date)
            self.incomes_list.append(new_income)

    def add_expenses(self, expenses, date):
        for expense in expenses:
            new_expense = Expense(expense['amount'], expense['category'], date)
            self.expenses_list.append(new_expense)
            self.expense_categories.append(new_expense.name)

    def generate_from_data(self, data):
        dates = data.keys()
        self.dates_list.extend(dates)

        for date in dates:
            incomes = data[date][0]['income']
            self.add_incomes(incomes, date)

            expenses = data[date][1]['expense']
            self.add_expenses(expenses, date)

    def save_changes(self, username):
        data = {}
        for income in self.incomes_list:
            if income.date not in data.keys():
                data[income.date] = []
            data[income.date].append(income)

        for expense in self.expenses_list:
            if expense.date not in data.keys():
                data[expense.date] = []
            data[expense.date].append(expense)

        with open("money_tracker_{}.txt".format(username), 'w') as f:
            for k, v in sorted(data.items()):
                f.write("=== {} ===\n".format(k))
                for item in v:
                    f.write("{}, {}, New {}\n".format(item.amount, item.name, item.type))


if __name__ == '__main__':
    main()
