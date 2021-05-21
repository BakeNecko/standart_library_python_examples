# Декоратор классов total_ordering () получает класс, который предоставляет
# некоторые из методов сравнения, и добавляет остальные методы
import functools
import inspect
from pprint import pprint


@functools.total_ordering
class MyObject:
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        print(f'testing __eq__({self.val}, {other})')
        return self.val == other.val

    def __gt__(self, other):
        print(f'testing __gt__({self.val}, {other.val})')
        return self.val > other.val


print('Methods:\n')
pprint(inspect.getmembers(MyObject, inspect.isfunction))

a = MyObject(1)
b = MyObject(2)

print('\nComparisons:')
for expr in ['a < b', 'a <= b', ' a == b', 'a >= b', 'a > b']:
    print('\n{:<6}:'.format(expr))
    result = eval(expr)
    print(f'result of {expr}: {result}')
    

