def show_details(name, f):
    """ Показать детали вызываемого объекта """
    print(f'{name}:')
    print(f'object: {f}')
    print('__name__:', end=' ')
    if hasattr(f, '__name__'):
        print(f.__name__)
    else:
        print('(no __name__)')
    print(f'__doc__ {repr(f.__doc__)}')
    print()
