import functools


def standalone(self: object, a=1, b=2):
    """ Автономная функция """
    print(f'called standalone with: self-{self} a-{a} b-{b}')
    if self is not None:
        print(f'self.attr - ', self.attr)


class MyClass:
    """  Демонстрационный класс functools """
    def __init__(self):
        self.attr = 'instance attribute'

    method1 = functools.partialmethod(standalone)
    method2 = functools.partial(standalone)

o = MyClass()

print('standalone')
standalone(None)
print()

print('method1 as partialmethod')
o.method1()
print()

print('method 2 as partial')
try:
    o.method2()
except TypeError as err:
    print(f'ERROR: {err}')
