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


def processing_count(word):
    vowels = 0
    consonant = 0
    for char in word.lower():
        if char.isalpha():
            if char in ['a', 'e', 'i', 'o', 'u', 'y']:
                vowels += 1
            else:
                consonant += 1
    return vowels, consonant


def fun(path, chars, *args):
    f = open(path, 'r')
    myset = set()
    for st in f.readlines():
        for char in chars:
            st = st.replace(char, '')
        vowel_consonant_counter = list()
        a = st.split(' ')
        for word in a:
            if word not in args:
                count = processing_count(word)
                if count not in vowel_consonant_counter:
                    vowel_consonant_counter.append(count)
                    myset.add(''.join(sorted(word)))
    print(len(myset))


fun("words.txt", 'dfj', 'dfgf', )
