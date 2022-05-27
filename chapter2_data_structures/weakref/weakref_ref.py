import weakref


class ExpensiveObject:

    def __dell__(self):
        print(f'(Deleting {self})')


if __name__ == '__main__':
    obj = ExpensiveObject()
    r = weakref.ref(obj)

    print('obj:', obj)
    print('ref:', r)
    print('r():', r())

    print('deleting obj')
    del obj
    print('r(): ', r())
