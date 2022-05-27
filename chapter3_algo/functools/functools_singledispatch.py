import functools

@functools.singledispatch
def myfunc(arg):
    print(f'default myfunc({arg})')


@myfunc.register(int)
def _(arg):  # myfunc_int
    print(f'myfunc_int({arg})')


@myfunc.register(list)
def _(arg):  # myfunc_list
    print(f'myfunc_list(): {arg}')


myfunc('string argument')
myfunc(1)
myfunc(2.3)
myfunc(['a', 'b', 'c'])
