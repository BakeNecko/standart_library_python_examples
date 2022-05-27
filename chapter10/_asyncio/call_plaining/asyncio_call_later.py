# 10.5.3.2 Планирование обратного вызова с задержкой во времени
"""
Чтобы отложить выполнение функции обратного вызова на более поздний момент времени,
следует исползовать метод call_later(). Его первым аргументом является длительность
задержки в секундах, вторым - функция обратного вызова.
"""
import asyncio


def callback(arg):
    print(f'callback {arg} invoked')


async def main(loop: 'asyncio.AbstractEventLoop'):
    print('registering callbacks')
    loop.call_later(0.2, callback, 1)
    loop.call_later(0.1, callback, 2)
    loop.call_soon(callback, 3)

    await asyncio.sleep(0.4)


if __name__ == '__main__':
    """
    В этом примере выполнение той же функции обратного вызова запланировано 
    на несколько различных моментов времени c разными аргументами. Вызов, 
    запланированный c помощью метода call_soon (), которому был передан аргумент 3, 
    выполняется раньше других, тем самым подтверждая тот факт, что планирование 
    вызова “на ближайшее время” обычно означает минимальную задержку
    """
    event_loop = asyncio.get_event_loop()
    try:
        print('entering event loop')
        event_loop.run_until_complete(main(event_loop))
    finally:
        print('closing event loop')
        event_loop.close()
