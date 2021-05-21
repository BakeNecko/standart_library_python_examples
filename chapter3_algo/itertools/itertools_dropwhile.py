# Функция dropwhile() создает итератор, который начинает воспроизводить
# элементы входного итератора сразу же после того, как для заданного условия будет получено ложное значение.
from itertools import dropwhile


def should_drop(x):
    print('Testing:', x)
    return x < 1


for i in dropwhile(should_drop, [-1, 0, 2, -2]):
    print('Yilding: ', i)
