from itertools import permutations


def show(iterable):
    first = None
    for i, item in enumerate(iterable, 1):
        if first != item[0]:
            if first is not None:
                print()
            first = item[0]
        print(''.join(item), end=' ')
    print()


if __name__ == '__main__':
    """
    Функция permutations () создает итератор, который возвращает все возможные
    перестановки заданной длины, образуемые из элементов входного итерируемого объекта.
    """

    print('All permutations:\n')
    show(permutations('abcd'))

    print('\nPairs:\n')
    show(permutations('abcd', r=2))
