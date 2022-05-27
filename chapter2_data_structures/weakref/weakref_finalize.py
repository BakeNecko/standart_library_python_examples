"""
2.8.3 Заверщающие операции при удалении объектов.
Надежность управления ресурсами при удалении слабых ссылок можно
повысить, связывая c объектами функции обратного вызова при помощи функции
finalize(). Экземпляр finalize (объект-финализатор) удерживается в памяти
до тех пор, пока не будет удален связанный c ним объект, даже если в приложении
отсутствуют ссылки на объект-финализатор.
"""
import weakref


class ExpensiveObject:

    def __del__(self):
        print(f'(Deleting {self})')


def on_finalize(*args):
    print('on_finalize({!r})'.format(args))


if __name__ == '__main__':
    obj = ExpensiveObject()
    weakref.finalize(obj, on_finalize, 'extra argument')
    del obj