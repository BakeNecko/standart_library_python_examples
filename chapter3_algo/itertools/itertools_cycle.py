# Функция cycle () создает итератор, повторяющий содержимое аргументов бесконечное количество раз.
from itertools import cycle

for i in zip(range(7), cycle(['a', 'b', 'c'])):
    print(i)
