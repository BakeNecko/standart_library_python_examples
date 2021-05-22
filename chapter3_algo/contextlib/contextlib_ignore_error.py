# Во многих случаях исключения, возбуждаемые библиотеками, удобно игноировать,
# если ошибка указывает на достижение определенного состояния или может
# быть проигнорирована по другим причинам. Наиболее распространеным
# способом игнорирования исключений является использование инструкции
# try:except, содержащей в блоке except только инструкцию pass
import contextlib


class NonFatalError(Exception):
    pass


def non_idempotent_operation():
    raise NonFatalError(
        'the operation failed because of existing state'
    )

try:
    print('trying non-idempotent operation')
    non_idempotent_operation()
    print('succeeded!')
except NonFatalError:
    pass

print('done')

# Форму try:except можно заменить формой contextlib.suppress () для болee
# явного подавления класса исключений, возникающих в пределах блока with.

with contextlib.suppress(RuntimeError, NonFatalError):
    print('trying non-idempotent operation')
    non_idempotent_operation()
    print('succeeded!')

print('done')
