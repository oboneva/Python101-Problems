import utils

class Term:
    def __init__(self, *, coefficient, variable, power):
        if power == 0:
            variable = None

        self.coefficient = coefficient
        self.variable = variable
        self.power = power

    def __eq__(self, other):
        return (
            self.coefficient == other.coefficient and
            self.variable == other.variable and
            self.power == other.power and
            self.constant == other.constant
        )

    def __str__(self):
        if self.is_constant:
            return str(self.coefficient)

        str_coefficient = ''
        str_power = ''

        if self.power > 1:
            str_power = f'^{self.power}'

        if self.coefficient > 1:
            str_coefficient = f'{self.coefficient}*'

        return f'{str_coefficient}{self.variable}{str_power}'

    def __repr__(self):
        return str(self)

    @property
    def is_constant(self):
        return self.variable is None and self.power == 0

    @classmethod
    def constant(cls, value):
        return cls(coefficient=value, variable=None, power=0)

    @classmethod
    def parse_from_string(cls, string):
        coefficient, variable, power = utils.extract_term(string)

        return cls(coefficient=coefficient, variable=variable, power=power)

    def __add__(self, other):
        if self.power != other.power:
            raise ValueError('Cannot add terms with different powers!')

        return Term(
            coefficient=self.coefficient + other.coefficient,
            variable=self.variable,
            power=self.power
        )

    def derivative(self):
        if self.is_constant:
            return Term.constant(0)

        return Term(
            coefficient=self.power * self.coefficient,
            variable=self.variable,
            power=max(0, self.power - 1)
        )


if __name__ == '__main__':
    main()
