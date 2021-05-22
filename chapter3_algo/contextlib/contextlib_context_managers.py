# Предоставленные экземпляру ExitStack менеджеры контекста обрабатываются
# так, как если бы они встречались в серии вложенных инструкций with.
# Ошибки, возникающие в пределах контекста, распространяются в соответствии
# c обычной процедурой обработки ошибок в менеджерах контекста.
import contextlib


class Tracker:
    """Базовый класс для менеджеров контекста, генерирующих ошибки"""

    def __init__(self, i):
        self.i = i

    def msg(self, s):
        print(f'{self.__class__.__name__}({self.i}): {s}')

    def __enter__(self):
        self.msg('entering')


class HandleError(Tracker):
    """ Если полученно искл., считать его обработанным """

    def __exit__(self, *exc_details):
        received_exc = exc_details[1] is not None
        if received_exc:
            self.msg('handling exception {!r}'.format(exc_details[1]))
        self.msg('exiting {}'.format(received_exc))
        # Возврат булевого значения, указывающего на то,
        # было ли обработано исключение
        return received_exc


class PassError(Tracker):
    """ Если получено искобчение, пекредать его дальше."""

    def __exit__(self, *exc_details):
        received_exc = exc_details[1] is not None
        if received_exc:
            self.msg('passing exception {!r}'.format(exc_details[1]))
        self.msg('exiting')
        # Возврат значения False, указывающего на то, что
        # исключение не было обработано
        return False


class ErrorOnExit(Tracker):
    """ Сгенерировать исключение """

    def __exit__(self, *exc_details):
        self.msg('throw error')
        raise RuntimeError(f'from {self.i}')


class ErrorOnEnter(Tracker):
    """ Сгенерировать исключение """

    def __enter__(self):
        self.msg('throwing error on enter')
        raise RuntimeError(f'from {self.i}')

    def __exit__(self, *exc_info):
        self.msg('exiting')


print('No errors:')


def variable_stack(handlers: list = []):
    with contextlib.ExitStack() as stack:
        for item in handlers:
            stack.enter_context(item)


variable_stack([
    HandleError(1),
    PassError(2),
])
print('\nError at the end of the context stack:')
variable_stack([
    HandleError(1),
    HandleError(2),
    ErrorOnExit(3)
])

print('\nError in the middle of the context stack:')
variable_stack([
    HandleError(1),
    PassError(2),
    ErrorOnExit(3),
    HandleError(4)
])

try:
    print('\nError ignored:')
    variable_stack([
        PassError(1),
        ErrorOnExit(2)
    ])
except RuntimeError:
    print('error handled outside of context')
