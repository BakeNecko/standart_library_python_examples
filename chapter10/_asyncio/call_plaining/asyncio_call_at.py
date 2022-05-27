# 10.5.3.3 Плнирование обратного вызова на определённое время
"""
Гакже существует возможность запланировать вызов на определенное время.
Используемый для этого цикл основывается на монотонных часах, а не на часах
истекшего времени, что исключает отнесение момента времен “сейчас” к
прошлому моменту времени. Чтобы выбрать время для запланированного обратного
вызова, необходимо вести отсчет от внутреннего состояния этих часов, используя
метод time() цикла
"""
import asyncio
import time

def callback(arg, loop):
    print(f'callback {arg} invoked at {loop.time()}')


async def main(loop: 'asyncio.AbstractEventLoop'):
    now = loop.time()
    print(f'clock time: {time.time()}')
    print(f'loop time: {now}')

    print('registering callbacks')
    loop.call_at(now + 0.2, callback, 1, loop)
    loop.call_at(now + 0.1, callback, 2, loop)
    loop.call_soon(callback, 3, loop)

    await asyncio.sleep(1)


if __name__ == '__main__':
    """
    Обратите внимание на то, что время, соответствующее часам цикла, 
    не совпадает со значением, возвращаемым функцией time.time()
    """
    event_loop = asyncio.get_event_loop()
    try:
        print('entering event loop')
        event_loop.run_until_complete(main(event_loop))
    finally:
        print('closing event loop')
        event_loop.close()
