import functools
from itertools import *
import operator
import pprint


@functools.total_ordering
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point (x={self.x}, y={self.y})'

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __gt__(self, other):
        return (self.x, self.y) > (other.x, other.y)


data = list(map(Point,
                cycle(islice(count(), 3)),
                islice(count(), 7)))
print('Data: ')
pprint.pprint(data, width=45)
print()

# Попытаться сгруппировать несортированные данные
# на основании значений Х
print('Grouped, unsorted:')
for k, g in groupby(data, operator.attrgetter('x')):
    print(k, list(g))
print()

# Сортировка данных
data.sort()
print('Sorted:')
pprint.pprint(data, width=35)
print()

# Чтобы группирование работало так, как ожидается, входная последовательность
# должна быть отсортированна по ключу
# Группирование сортированных данных на основании значений Х
print('Grouped, sorted:')
for k, g in groupby(data, operator.attrgetter('x')):
    print(k, list(g))
print()
