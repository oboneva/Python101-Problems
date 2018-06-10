class InvalidOptionFromMenuError(BaseException):
    def __init__(self):
        self.message = 'Invalid option!'


class MoneyTrackerMenu:
    menu_options = ['show all data',
                    'show data for specific date',
                    'show expenses ordered by categories',
                    'add new income',
                    'add new expense',
                    'exit']

    def __init__(self, username, money_tracker):
        self.money_tracker = money_tracker
        self.username = username
        print('Hello, {}'.format(username))
        self.choose()

    def choose(self):
        self.display_menu_options()
        option = self.choose_from_menu()
        self.processing_chosen_option(option)

    def display_menu_options(self):
        print('Choose one of the following options to continue:')
        for i in range(1, 7):
            print("{} - {}".format(i, self.menu_options[i - 1]))

    def choose_from_menu(self):
        while True:
            try:
                option = int(input())
                if option <= 0 or option > 6:
                    raise InvalidOptionFromMenuError()
            except ValueError:
                print('Enter number!')
            except InvalidOptionFromMenuError:
                print('Ooops, options are from 1 to 6!')
            else:
                break

        return option

    def processing_chosen_option(self, option):
        if option == 1:
            self.money_tracker.show_all_data()
            print("")
        elif option == 2:
            self.money_tracker.show_data_for_specific_date()
            print("")
        elif option == 3:
            self.money_tracker.show_expenses_ordered_by_category()
            print("")
        elif option == 4:
            self.money_tracker.add_income(self.username)
            print("")
        elif option == 5:
            self.money_tracker.add_expense(self.username)
            print("")
        else:
            print("Goodbye!")
            return

        self.choose()

if __name__ == '__main__':
    main()
