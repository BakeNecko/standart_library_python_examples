import functools
from utils import show_details


class MyClass:
    """ Демонстрационный класс для functools """
    def __call__(self, e, f=6, *args, **kwargs):
        """ Docstring for MyClass.__call__ """
        print(f'called object with: self-{self} e-{e} f-{f}')


o = MyClass()

show_details('instance', o)
o('e goes here')
print()

p = functools.partial(o, e='default for e', f=8)
functools.update_wrapper(p, o)
show_details('instance wrapper', p)
p()
