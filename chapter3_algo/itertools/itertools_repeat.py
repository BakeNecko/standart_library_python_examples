# repeat() создает итератор, возращающий одно и тоже значение при каждом обращении к нему
from itertools import repeat

for i in repeat('over-and-over', 5):
    print(i)
