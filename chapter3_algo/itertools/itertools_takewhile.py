# takewhile создает итератор, который выдает элементы
# из входного итератора, пока тестирующая функция возвращает истинное значение.
from itertools import takewhile


def should_take(x):
    print('Testing:', x)
    return x < 1


for i in takewhile(should_take, [-1, 0, 1, 2, -2]):
    print('Yilding:', i)
