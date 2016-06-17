# Реализовать функцию to_json(obj),
# которая на вход
# получает python объект,
# а на выходе у неё строка в формате JSON.
# А еще получает неотрицательную переменную indent,
# которая определяет количество отступов,
# для каждого уровня вложенности.


def to_json(obj, indent=1):
    space = ' '*indent
    if obj is None:
        return 'null'
    elif isinstance(obj, (list, tuple)):
        if len(obj) == 0:
            return '[]'
        else:
            s = '[' + to_json(obj[0], indent)
            s = '[' + to_json(obj[0], indent)
            for i in range(1, len(obj)):
                s += ',' + to_json(obj[i], indent)
            return s + ']'
    elif isinstance(obj, dict):
        if len(obj) == 0:
            return '{}'
        else:
            items = iter(obj.items())
            temp = next(items)
            s = '{' + to_json(temp[0], indent) + ': ' + to_json(temp[1], indent)
            for item in items:
                s += ',' + to_json(item[0], indent) + ': ' + to_json(item[1], indent)
            return s + '}'
    elif isinstance(obj, bool):
        return str(obj).lower()
    elif isinstance(obj, (int, float)):
        return str(obj)
    elif isinstance(obj, str):
        return '"' + obj.replace('"', r'\"').replace('\n', r'\\n').replace('\t', r'\\t') + '"'
    else:
        if hasattr(obj, '__dict__'):
            return to_json(obj.__dict__, indent)
        else:
            raise TypeError('This type {type} can\'t be parsed.'.format(type=str(type(obj))))


class Aggregator:
    def __init__(self):
        self.total_sum = (15, 45, (15, 48))
        self.elements_count = 0.5e5
        self.dict = {"a":15, "c":5}

    def add_value(self, value):
        self.total_sum += value
        self.elements_count += 1

    def get_average(self):
        return self.total_sum / self.elements_count

    def get_sum(self):
        return self.total_sum


def main():
    a = Aggregator()
    try:
        print(to_json(a, 5))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
