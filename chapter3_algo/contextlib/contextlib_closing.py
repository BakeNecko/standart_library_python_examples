# 3.4.4
# Класс file обеспечивает непосредственную поддержкуАР1 менеджера контекста,
# однако в случае других объектов, представляющих открытые дескрипторы, это не так.
# В разделе документации стандартной библиотеки, посвященном модулю
# contextlib, в качестве примера представлен объект, возвращаемый вызовом
# urllib.urlopen (). Некоторые другие устаревшие классы используют метод
# close (), но не поддерживаютАР1 менеджера контекста. Гарантированное закрытие
# дескриптора обеспечивается созданием для него менеджера контекста c помощью
# функции closing ().
import contextlib


class Door:
    def __init__(self):
        print('__init__()')
        self.status = 'open'

    def close(self):
        print('close()')
        self.status = 'closed'


print('Normal Example:')
with contextlib.closing(Door()) as door:
    print(f'inside with statement: {door.status}')
print(f'outside with statement: {door.status}')

print('\nError handling example:')
try:
    with contextlib.closing(Door()) as door:
        print('raising from inside with statement')
        raise RuntimeError('error message')
except Exception as err:
    print('Hand and error', err)
print(f'outside with statement: {door.status}')
