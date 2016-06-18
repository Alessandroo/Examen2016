# Реализовать функцию to_json(obj),
# которая на вход
# получает python объект,
# а на выходе у неё строка в формате JSON.
# А еще получает неотрицательную переменную indent,
# которая определяет количество отступов,
# для каждого уровня вложенности.


import json


def to_json(obj, indent=1, lvl=0):
    result = ''
    space = ' ' * indent

    if isinstance(obj, (list, tuple)):
        result += space * lvl + '[\n'

        for i in obj:
            result += to_json(i, indent, lvl + 1) + ',\n'

        result = result[:-2] + '\n' + space * lvl + ']'
    elif isinstance(obj, dict):
        result += space * lvl + '{\n'

        for item in obj.items():
            result += to_json(item[0], indent, lvl + 1) + ': ' + to_json(item[1], indent, 0) + ',\n'

        result = result[:-2] + '\n' + space * lvl + '}'
    elif isinstance(obj, bool):
        result += space * lvl

        if obj:
            result += 'true'
        else:
            result += 'false'
    elif isinstance(obj, (int, float)):
        result += space * lvl
        result += str(obj)
    elif isinstance(obj, str):
        obj = obj.replace('\\', '\\\\')
        obj = obj.replace('\n', '\\n')
        obj = obj.replace('\"', '\\"')
        obj = obj.replace('\t', '\\t')

        result += space * lvl
        result += '\"' + obj + '\"'
    elif obj is None:
        result += space * lvl
        result += 'null'
    else:
        raise TypeError('Wrong type')

    return result


class Aggregator:
    def __init__(self):
        self.total_sum = (15, 45, (15, 48))
        self.elements_count = 0.5e5
        self.dict = {"a": 15, "c": 5}


def main():
    a = Aggregator()
    x = [1, 2, 2.5e5, 'asd\nas', False, None, {1: True, 2: False}, [123, [1, 2, 3]]]
    try:
        print(json.dumps(x))
        print("\n\n\n")
        print(to_json(x, 4))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
