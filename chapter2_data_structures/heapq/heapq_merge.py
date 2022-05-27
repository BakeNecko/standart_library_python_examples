"""
2.4.5 Эфф. слияение отсорт. последовательностей
list(sorted(itertools.chain(*data))) # Эфф. для не больших наборов данных.
merge() # исп. кучу для генерации новой последовательности по одному эл. за раз, исп.
          для определения очередного эл. памят фиксированного объема. Т.к merge исп кучу
          расход памяти зависит от кол. объединяемых последователностий, а не от кол-ва
          эл-ов в каждой их них.
"""

import heapq
import random

if __name__ == '__main__':

    random.seed(2016)

    data = []
    for i in range(4):
        new_data = list(random.sample(range(1, 101), 5))
        new_data.sort()
        data.append(new_data)

    for i, d in enumerate(data):
        print('{}: {}'.format(i, d))

    print('\nMerged:')
    for i in heapq.merge(*data):
        print(i, end=' ')
    print()
