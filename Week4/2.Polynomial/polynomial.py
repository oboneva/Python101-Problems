from term import Term

class Polynomial:
    def __init__(self, terms):
        self._terms = {}

        for term in terms:
            self.add_term(term)

    def add_term(self, term):
        if term.power is None:
            term.power = 0

        if term.power not in self._terms:
            self._terms[term.power] = term
        else:
            self._terms[term.power] += term

    def __str__(self):
        sorted_terms = []

        for term_power in sorted(self._terms.keys(), reverse=True):
            sorted_terms.append(str(self._terms[term_power]))

        return " + ".join(sorted_terms)

    @classmethod
    def parse_from_string(cls, s):
        unparsed_terms = s.split('+')

        terms = [
            Term.parse_from_string(t) for t in unparsed_terms
        ]

        return cls(terms)

    def differentiation(self):
        result = []

        for k, v in sorted(self._terms.items(), reverse=True):
            d = v.derivative()
            if d.coefficient != 0 or len(result) == 0:
                result.append(str(d))

        return " + ".join(result)


if __name__ == '__main__':
    main()
