from operator import *


class MyObj:
    """ Пример перегрузки операторов """
    def __init__(self, val):
        super(MyObj, self).__init__()
        self.val = val

    def __str__(self):
        return f'MyObj({self.val})'

    def __lt__(self, other):
        print(f'Testing {self} < {other}')

    def __add__(self, other):
        print(f'Adding {self} + {other}')
        return MyObj(self.val + other.val)

a = MyObj(1)
b = MyObj(2)

print('Comparison:')
print(lt(a, b))
print('\nArithmetic:')
print(add(a, b))
