from datetime import datetime
from income import Income
from expense import Expense


class MoneyTracker:
    def __init__(self, aggregated_object):
        self.aggregated_object = aggregated_object

    def show_expenses_for_date(self, date, expenses):
        for expense in self.aggregated_object.expenses_list:
            if expense.date == date:
                print("{}, {}, New Expense".format(expense.amount, expense.name))

    def show_incomes_for_date(self, date, incomes):
        for income in incomes:
            if income.date == date:
                print("{}, {}, New Income".format(income.amount, income.name))

    def show_data_for_date(self, date):
        print("=== {} ===".format(date))
        self.show_incomes_for_date(date, self.aggregated_object.incomes_list)
        self.show_expenses_for_date(date, self.aggregated_object.expenses_list)

    def show_all_data(self):
        for date in self.aggregated_object.dates_list:
            self.show_data_for_date(date)

    def show_data_for_specific_date(self):
        while True:
            try:
                date = str(input("Enter date in the following format 'dd-mm-yyyy'\n>>>>: "))
                if date not in self.aggregated_object.dates_list:
                    raise Exception
                else:
                    break
            except Exception:
                print("Invalid date or format!")

        self.show_data_for_date(date)

    def show_expenses_ordered_by_category(self):
        ordered_by_category = {}

        for expense in self.aggregated_object.expenses_list:
            if expense.name in ordered_by_category.keys():
                ordered_by_category[expense.name].append(expense)
            else:
                ordered_by_category[expense.name] = []
                ordered_by_category[expense.name].append(expense)

        for k, v in sorted(ordered_by_category.items()):
            print("=== {} ===".format(k))
            for item in v:
                print("{} {}".format(item.amount, item.date))

    def gather_info(self, category_type='income'):
        while True:
            try:
                amount = float(input('New {} amount: '.format(category_type)))
                if amount <= 0:
                    raise ValueError
                break
            except TypeError:
                print("The amount must be integer or decimal!")
            except ValueError:
                print("The amount must be positive number!")

        category_name = str(input('New {} type: '.format(category_type)))

        while True:
            try:
                date = input("New {} date in the following format 'dd-mm-yyyy': ".format(category_type))
                datetime.strptime(date, "%d-%m-%Y")
                break
            except ValueError:
                print('Invalid date or format!')

        return (amount, category_name, date)

    def add_income(self, username):
        amount, category_name, date = self.gather_info(category_type='income')
        new_income = Income(amount, category_name, date)
        self.aggregated_object.incomes_list.append(new_income)
        if date not in self.aggregated_object.dates_list:
            self.aggregated_object.dates_list.append(date)
        self.aggregated_object.save_changes(username)

    def add_expense(self, username):
        amount, category_name, date = self.gather_info(category_type='expense')
        new_expense = Expense(amount, category_name, date)
        self.aggregated_object.expenses_list.append(new_expense)
        if date not in self.aggregated_object.dates_list:
            self.aggregated_object.dates_list.append(date)
        self.aggregated_object.save_changes(username)


if __name__ == '__main__':
    main()
