# *функция merge_longer_iter(iterables*, fill)
# возвращает итератор из кортежей элементов передаваемых iterable-объектов,
#  объединенных по позиции (сначала первые из первых, вторые из вторых и тд).
#  Итератор выдает кортежи, пока не закончится самый длинный iterable.
#  Если один из них заканчивается, то вместо его элементов вставляется fill

from itertools import chain, repeat


class ZipExhausted(Exception):
    pass


def izip_longest(*args, **kwds):
    # izip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
    fillvalue = kwds.get('fillvalue')
    counter = [len(args) - 1]

    def sentinel():
        if not counter[0]:
            raise ZipExhausted
        counter[0] -= 1
        yield fillvalue
    fillers = repeat(fillvalue)
    iterators = [chain(it, sentinel(), fillers) for it in args]
    try:
        while iterators:
            yield tuple(map(next, iterators))
    except ZipExhausted:
        pass


for i in izip_longest([1, 4, 7], [2, 5, 8, 9, 10], [3, 6], fillvalue='-'):
    print(i)