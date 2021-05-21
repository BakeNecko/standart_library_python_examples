import functools


@functools.singledispatch
def myfunc(arg):
    print(f'default myfunc({arg})')


@myfunc.register(int)
def myfunc_int(arg):
    print(f'myfunc_int({arg})')


@myfunc.register(list)
def myfunc_list(arg):
    print(f'myfunc_list(): {arg}')


myfunc('string argument')
myfunc(1)
myfunc(2.3)
myfunc(['a', 'b', 'c'])
