num_literal_regex = '(\d+(.\d*)?)'
str_literal_regex = '("|\')(.*)\1'

valid_token_literals = [
    ('+', 'plus'), (num_literal_regex, 'num'), (str_literal_regex, 'str'),
    ('\((.+)\)', 'parents')
]


class Token:
    elements = None

    def __init__(self, *elements):
        self.elements = elements

    def __str__(self):
        return str(self.elements)

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        if type(other) is not type(self):
            raise ValueError(str(other), 'is not of type', str(type(self)))
        return self.value() + other.value()

    def value(self):
        return self.elements


class Plus(Token):
    def value(self):
        r = 0
        for e in self.elements:
            r += e
        return r


class Num(Token):
    def __init__(self, i: str):
        if i.isalnum():
            self.elements = float(i)
        else:
            raise ValueError('Input string is not of type num ("' + i + '")')

    def value(self):
        return self.elements


class Str(Token):
    def __init__(self, i: str):
        self.elements = i

    def value(self):
        return self.elements


class Parenthesis(Token):
    def __init__(self, e: Token):
        self.elements = e

    def value(self):
        return self.elements.value()
