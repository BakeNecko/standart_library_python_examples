# От генератора к менеджеру контекста 3.4.3

import contextlib


@contextlib.contextmanager
def make_context():
    print('entering')
    try:
        yield 'ok'
    except RuntimeError as err:
        print('ERROR:', err)
    finally:
        print('exiting')


print('Normal:')
with make_context() as value:
    print('value - ', value)
    print('inside with statement:', value)

print('\nHandled error:')
with make_context() as value:
    print('value - ', value)
    raise RuntimeError('showing example of handling an error')

print('\nUnhandled error:')
with make_context() as value:
    print('value - ', value)
    raise ValueError('this exception is not handled  ')
