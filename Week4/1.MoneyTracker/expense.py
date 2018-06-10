from category import Category

class Expense(Category):
    def __init__(self, amount, name, date):
        super().__init__(amount, name, date)
        self.type = 'Expense'

    def __str__(self):
        return '{} - {}'.format(super().__str__(), self.type)

    def __repr__(self):
        return '{} - {}'.format(super().__repr__(), self.type)

    def __eq__(self, other):
        return super().__eq__(other)

if __name__ == '__main__':
    main()
