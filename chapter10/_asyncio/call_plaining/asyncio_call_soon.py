# 10.5.3.1 Планирование обратного вызова "на ближайшее время"
"""
Если точно время выполнения обратных вызовов не имеет значения, метод
call_soon() позволяет запланировать вызов на следующую итерацию цикла.
При запуске функции обратного вызова ей передаются любые дополнительные
позиционные аргументы, указанные вслед за функцией обратного вызова при
выполнении метода call_soon(). Передать функции обратного вызова key-аргументы
аргументы можно с помощью функции partial() из модуля functools (см 3.1)
"""
import asyncio
import functools


def callback(arg, *, kwarg='default'):
    print(f'callback invoked with {arg} and {kwarg}')


async def main(loop: 'asyncio.AbstractEventLoop'):
    print('registering callbacks')
    loop.call_soon(callback, 1)
    wrapped = functools.partial(callback, kwarg='not default')
    loop.call_soon(wrapped, 2)
    await asyncio.sleep(0.1)


if __name__ == '__main__':
    """
    Функции обратного вызова запускаются в том порядке, в каком они были запланированы.
    """
    event_loop = asyncio.get_event_loop()
    try:
        print('entering event loop')
        event_loop.run_until_complete(main(event_loop))
    finally:
        print('closing event loop')
        event_loop.close()
