# 10.5.7.1 Блокироваки
"""
Класс Lock можно использовать для защиты доступа к разделяемым ресурсам.
Лишь владелец блокировки может использовать ресурс. Несколько одновременных
попыток получить блокировку будут блокироваться, поэтому в каждый момент времени
блокировка может иметь только одного владельца.
"""
import asyncio
import functools


def unlock(lock: 'asyncio.Lock'):
    print('callback releasing lock')
    lock.release()


async def coro1(lock: 'asyncio.Lock'):
    print('coro1 waiting for the lock')
    async with lock:  # В книге `with await lock:` Но это не верно в 3.9+
        print('coro1 acquired lock')
    print('coro1 released lock')


async def coro2(lock: 'asyncio.Lock'):
    print('coro2 waiting for the lock')
    await lock.acquire()
    try:
        print('coro2 acquired lock')
    finally:
        print('coro2 released lock')
        lock.release()


async def main(loop: 'asyncio.AbstractEventLoop'):
    # Создать и получить разделяемую блокировку
    lock = asyncio.Lock()
    print('acquiring the lock before starting coroutines')
    await lock.acquire()
    print(f'lock acquired: {lock.locked()}')

    # Запланировать функцию обратного вызова для
    # отмены блокировки
    loop.call_later(2, functools.partial(unlock, lock))

    # Запустить сопрограммы, которые хотят использовать
    # блокировку
    print('waiting for coroutines')
    await asyncio.wait([coro1(lock), coro2(lock)])


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main(event_loop))
    finally:
        print('close event_loop')
        event_loop.close()
