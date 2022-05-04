# 10.5.7.2 События
"""
ласс asyncio.Event основан на классе threading.Event и позволяет нескольким
потребителям ожидать наступления какого-либо события без отслеживания
конкретного значения, связанного с соответствующим уведомлением.
"""
import asyncio
import functools


def set_event(event):
    print('setting event in callback')
    event.set()


async def coro1(event: 'asyncio.Event'):
    print('coro1 waiting for event')
    await event.wait()
    print('coro1 triggered')


async def coro2(event: 'asyncio.Event'):
    print('coro2 waiting for event')
    await event.wait()
    print('coro2 riggered')


async def main(loop: 'asyncio.AbstractEventLoop'):
    # Создать разделяемое событе
    event = asyncio.Event()
    print(f'event start state: {event.is_set()}')

    loop.call_later(1, functools.partial(set_event, event))

    await asyncio.wait([coro1(event), coro2(event)])
    print(f'event end state: {event.is_set()}')


if __name__ == '__main__':
    """
    Как и в случае класса Lock, сопрограммы coro1() и coro2() ожидаютустановки 
    события. Отличие заключается в том, что выполнение обеих сопрограмм может 
    начаться сразу же, как только событие изменит состояние, и они не должны
    становиться единоличными владельцами объекта события.
    """
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main(event_loop))
    finally:
        event_loop.close()
