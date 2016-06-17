# Класс “линейная функция”.
# И основные ее операции:
# -вычисление в точке,
# -сложение с другой линейной функцией,
# -умножение на константу,
# -композиция с другой линейной функцией, -
# строковое представление.
# Нужно уточнить формулировку, но суть примерно такая.


class LinearFunction:
    def __init__(self, function):
        self.function = function

    def __add__(self, other):
        if isinstance(other, LinearFunction):
            self.function = lambda x: self.function(x) + other.function(x)
            return self
        else:
            raise TypeError("Function can be added only with other function")

    def __call__(self, *args, **kwargs):
        return self.function(args[0])

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.function = lambda x: self.function(x* other)
            return self
        else:
            raise TypeError("Function can be multiple only on number")

    def compose(self, g):
        return LinearFunction(lambda a: self.function(g(a)))

    def __str__(self):
        return "Y = {0}".format(self.function)


def main():
    y1 = LinearFunction(lambda x: x*2 + 5)
    print(type(y1))
    y1 = y1 + y1
    print(y1(5))
    y2 = LinearFunction(lambda x: 4*x)
    print(y2(10))
    # y3 = y2.compose(y1)
    # print(y3(10))
    print(type(y1))
    print(y1)


if __name__ == '__main__':
    main()
