# 10.5.2.4 Генераторы вместо сопрограмм
"""
Функции сопрограмм являются ключевым элементом модуля asyncio. Они
предоставляют языковую конструкцию, позволяющую останавливать выполнение
части программы, сохранять состояние этого вызова и осуществлять повторное
вхождение в это же состояние в более поздний момент времени. Для фреймворка
параллелизма важна возможность выполнения любого из этих действий.
Возможность определять сопрограммы c помощью инструкции async def и
уступать управление c помощью ключевого слова await, как это делалось в
приведенных выше примерах, появилась в версии Python 3.5. В предыдущих версиях
Python 3 тот же эффект достигается за счет использования функций-генераторов,
обернутых декоратором asyncio. coroutine(), и инструкции yield from.
"""
import asyncio


@asyncio.coroutine
def outer():
    print('in outer')
    print('waiting for result1')
    result1 = yield from phase1()
    print('waiting for result2')
    result2 = yield from phase2()
    return result1, result2


@asyncio.coroutine
def phase1():
    print('in phase1')
    return 'result1'


@asyncio.coroutine
def phase2(arg):
    print('in phase2')
    return f'result2 derived from {arg}'


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    try:
        return_value = event_loop.run_until_complete(outer())
        print('return value: {!r}'.format(return_value))
    finally:
        event_loop.close()
