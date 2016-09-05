# *функция niter(iterable, n=2)
# возвращает кортеж из "копий"-итераторов по переданному итератору,
#  каждый итератор должен предоставлять то же, что и итератор-источник.
#  Новые итераторы независимы в смысле их текущих позиций (в первом может вычитаться значение,
#  а в последующих они неизменны, возвращают первое значение)

import collections


def niter(iterable, n=2):
    it = iter(iterable)
    deques = [collections.deque() for i in range(n)]

    def gen(my_deque):
        while True:
            if not my_deque:
                try:
                    new_val = next(it)
                except StopIteration:
                    return
                for d in deques:
                    d.append(new_val)
            yield my_deque.popleft()

    return tuple(gen(d) for d in deques)


a = [1, 2, 3, 4]
ab = niter(a, 8)
print(ab)
