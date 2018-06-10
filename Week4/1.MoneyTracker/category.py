class Category:
    def __init__(self, amount, name, date):
        if amount < 0:
            raise ValueError('The amount must be positive!')
        if type(amount) is not float and type(amount) is not int:
            raise TypeError('The amount must be integer or float!')

        self.name = name
        self.amount = amount
        self.date = date

    def __str__(self):
        return '{}$ - {} - {}'.format(self.amount, self.name, self.date)

    def __repr__(self):
        return '{}$ - {} - {}'.format(self.amount, self.name, self.date)

    def __eq__(self, other):
        return self.amount == other.amount and self.name == other.name and self.date == other.date

if __name__ == '__main__':
    main()
