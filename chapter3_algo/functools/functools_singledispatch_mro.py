import functools


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B):
    pass


class E(C, D):
    pass


@functools.singledispatch
def myfunc(arg):
    print(f'default myfunc({arg.__class__.__name__})')


@myfunc.register(A)
def myfunc_A(arg):
    print(f'myfunc_A({arg.__class__.__name__})')


@myfunc.register(B)
def myfunc_B(arg):
    print(f'myfunc_B({arg.__class__.__name__})')


@myfunc.register(C)
def myfunc_C(arg):
    print(f'myfunc_C({arg.__class__.__name__})')


myfunc(A())
myfunc(B())
myfunc(C())
myfunc(D())
myfunc(E())