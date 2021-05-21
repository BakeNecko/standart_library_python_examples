# Чтобы ограничить круг значений уникальными сочетаниями, а не перестановками,
# используйте функцию combinations (). Коль скоро все элементы входной
# последовательности являются уникальными, выходные последовательности не
# будут включать повторяющихся значений.
from itertools import combinations


def show(iterable):
    first = None
    for i, item in enumerate(iterable):
        if first != item[0]:
            if first is not None:
                print()
            first = item[0]
        print(''.join(item), end=' ')
    print()


print('Unique pairs:\n')
show(combinations('abcd', r=2))
