# Написать дескриптор RemoteResult(source_type, source_path, parser), который при чтении
# будет запрашивать результат по следующему правилу:
#
# Если source_type равен "file", то данные берутся из файла по пути source_path. Ф-ция parser
# предоставляется пользователем и имеет формат parser(data, line), где data - dict(), в котором
# можно хранить состояние между вызовами parser для каждой отдельной строки, а line - очередная
# считываемая строка. Если line равна None, то parser должен вернуть преобразованный dict() с учётом
# новой строки. Если line не равна None, то парсер должен вернуть результат обработки всех полученных
# данных. В результате попытки чтения данных из дескриптора, данные из source_path должны быть
# преобразованы в некоторое значение, которое зависит от реализации parser.
#
# Если source_type равен "url", то данные получаются удаленно с помощью GET http-запроса по адресу
# source_path. parser аналогичен прошлому пунктуи разбирает текст ответа построчно.
import urllib.request


class RemoteResult:
    def __init__(self):
        self.type = None
        self.path = None
        self.parser = None
        self.date = None

    def __get__(self, instance, owner):
        print('getter')
        cash = dict()
        for line in self.date:
            cash = parser(cash, line)
        return cash

    def __set__(self, instance, value):
        self.type = value.source_type
        self.path = value.source_path
        self.parser = value.parser
        print(self.type, self.path, self.parser)
        lines = []
        if self.type == 'file':
            with open(self.path) as file:
                for line in file.readlines():
                    lines.append(line)

        if self.type == 'url':
            page = urllib.request.urlopen(self.path)
            for line in page.readlines():
                lines.append(line)
        self.date = lines


class MyClass:
    x = RemoteResult()


def parser(date, line):
    if line is None:
        print(None)
        return date
    else:
        date[line] = line.upper()
        return date


m = MyClass()


class Mio:
    def __init__(self):
        self.source_type = 'url'
        self.source_path = 'https://github.com/Alessandroo/Myts/blob/master/Laba1/Task/Zad2.py'
        self.parser = parser


m.x = Mio()
print(m.x)
