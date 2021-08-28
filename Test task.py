class NumberFormatter:
    def __init__(self, *args):
        self.args = args

    def parseInt(self, s):

        array_of_number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        result = 0
        sign = 1
        substring = s

        if s[0] == '+':
            substring = s[1:]

        elif s[0] == '-':
            sign = -1
            substring = s[1:]

        power = len(substring) - 1

        for i in substring:
            result += array_of_number.index(i) * 10 ** power
            power -= 1

        return result * sign


Person = NumberFormatter()
print(Person.parseInt('+12345'))
