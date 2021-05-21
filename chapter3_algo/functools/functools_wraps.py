import functools
from utils import show_details


def simple_decorator(f):
    @functools.wraps(f)
    def decorated(a='decorated defaults', b=1):
        print(f'decorated: a-{a} b-{b}')
        print(' ', end=' ')
        return f(a, b=b)

    return decorated


def myfunc(a, b=2):
    """myfunc() is not complicated"""
    print(f'myfunc: a-{a} b-{b}')
    return


# Исходная функция
show_details('myfunc', myfunc)
myfunc('unwrapped, default b')
myfunc('unwrapped, passing b', 3)
print()

# Явное упаковывание
wrapped_myfunc = simple_decorator(myfunc)
show_details('wrapped_myfunc', wrapped_myfunc)
wrapped_myfunc()
wrapped_myfunc('args to wrapped', 4)
print()


# Упаковывание с помощью снитаксиса декоратора
@simple_decorator
def decorated_myfunc(a, b):
    """ decorated string """
    myfunc(a, b)
    return


show_details('decorated_myfunc', decorated_myfunc)
decorated_myfunc()
decorated_myfunc('args to decorated', 4)
