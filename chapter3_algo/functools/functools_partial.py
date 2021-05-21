import functools
from utils import show_details


def myfunc(a, b=2):
    "Docstring for myfunc()"
    print(f'called myfunc with: a-{a} b-{b}')


show_details('myfunc', myfunc)
p1 = functools.partial(myfunc, b=4)
show_details('raw wrapper', p1)

print('Updating wrapper:')
print('assign: ', functools.WRAPPER_ASSIGNMENTS)
print('assign: ', functools.WRAPPER_UPDATES)
print()

functools.update_wrapper(p1, myfunc)
show_details('updated wrapper', p1)
