class Context:
    def __init__(self):
        print('__init__()')

    def __enter__(self):
        print('__enter__()')
        return self

    def __exit__(self, *args, **kwargs):
        print('args - ', args)
        print('kwargs - ', kwargs)
        print('__exit__()')


c = Context()
with c:
    print('Doing work in the context')
