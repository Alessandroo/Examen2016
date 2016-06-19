# 4 (для особенно везучих).
# Консольная программа.
# Принимает 2 аргумента: текстовый файл с задачами, количество процессов.
# В текстовом файле описаны задачи. Описание задачи: <задача>\t<аргументы>.
# Каждая строка – задача. Всего 2 типа задач:
# -посчитать количество чётных чисел на промежутке,
# -проверка числа на простоту.
# Результаты работы программы вывести в файлы task1.out, ... taskn.out.
# Итого: нужно прочитать таски, распределить их по процессам,
# результат работы процессов записать в файлы.
# Количество выходных файлов равно количеству процессов.
import argparse
from multiprocessing import Pool


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2

    d = 3

    while d * d <= n and n % d != 0:
        d += 2

    return d * d > n


def count_numbers(a, b):
    return (b - a + 1) // 2 + (0 if a % 2 or b % 2 else 1)


def perform_task(task_with_index):
    index = task_with_index[0]
    task = task_with_index[1].split()
    if task[0] == 'count':
        res = count_numbers(*map(int, task[1:]))
    elif task[0] == 'prime':
        res = is_prime(int(task[1]))
    with open("task{0}.out".format(index), 'w') as f:
        f.write("{0} -> {1}".format(task_with_index[1], res))


def main(args):
    f = args.file
    count = args.count
    if count <= 0:
        raise ValueError("amount of processes must be positive")
    tasks = f.read().split('\n')
    tasks = [(i, tasks[i]) for i in range(len(tasks))]
    with Pool(processes=count) as pool:
        pool.map(perform_task, tasks)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('r'), help='input file')
    parser.add_argument('count', type=int, help='amount of processes')
    args = parser.parse_args()
    if args:
        main(args)
