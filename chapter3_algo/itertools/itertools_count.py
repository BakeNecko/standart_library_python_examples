# Функция count () создает итератор, вырабатывающий бесконечную последвательность целых чисел.
from itertools import count
import fractions

for i in zip(count(1), ['a', 'b', 'c']):
    print(i)

# With step and stop
start = fractions.Fraction(1, 3)  # 1/3
step = fractions.Fraction(1, 3)  # 1/3

for i in zip(count(start, step), ['a', 'b', 'c']):
    print('{}: {}'.format(*i))




