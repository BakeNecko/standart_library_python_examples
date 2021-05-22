# 3.4.7
# Большинство менеджеров контекста работает каждый раз c одним объектом,
# таким как дескриптор одиночного файла или базы данных. В подобных случаях
# объект известен заранее, и код, использующий менеджер контекста, может центрироваться
# вокруг этого объекта. Однако в других случаях программа может нуждаться
# в создании неизвестного количества объектов, для которых необходимо
# предусмотреть освобождение неиспользуемых ресурсов при покидании контекста.
# Именно для таких динамических случаев и создавался стек ExitStack.

# Экземпляр ExitStack поддерживает структуру данных для хранения функций
# обратного вызова, обеспечивающих очистку ресурсов. Эти функции помещаются
# в стек явным образом внутри контекста и при покидании контекста потоком
# управления вызываются в обратном порядке. Результат выглядит так, как если бы
# использовалисьдинамически устанавливаемые вложенные инструкции with.
import contextlib


@contextlib.contextmanager
def make_context(i):
    print(f'{i} entering')
    yield {}
    print(f'{i} exiting')


class Context:
    def __enter__(self):
        print('__enter__()')
        return self

    def __exit__(self, *args, **kwargs):
        print('args - ', args)
        print('kwargs - ', kwargs)
        print('__exit__()')


def variable_stack(n, msg):
    with contextlib.ExitStack() as stack:
        for i in range(n):
            stack.enter_context(make_context(i))
        print(msg)


variable_stack(2, 'inside context')
