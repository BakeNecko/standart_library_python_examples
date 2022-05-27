# 10.5.13 Получение сигналов Unix
"""
Обычно уведомления о системных событиях Unix прерывают работу приложений,
запуская соответствующие обработчики событий. При работе с модулем
asyncio выполнение обратных вызовов обработчиков сигналов чередуется с
выполнением други сопрограмм и функций обратного вызова, управляемых циклом событий.
Подобная интеграция приводит к уменьшению числа прерываемых функций и
минимизирует потребность в специальных мерах по защите ресурсов
в случае прерывания операций. Обработчики сигналов должны быть
обычными вызываемыми объектами, а не сопрограммами.
"""
import asyncio
import functools
import os
import signal


def signal_handler(name):
    print('signal_handler {!r}'.format(name))


async def send_signals():
    """
    В этом примере программа использует сопрограмму для отправки сигналов самой
    себе посредством вызова os.kill(). После отправки каждого сигнала программа
    уступаетуправление, обеспечивая возможность выполнения обработчика.
    В реальном приложении код будет содержать больше мест, в которых управление
    будет уступаться циклу событий, поэтому предпринимать какие-либо
    искусственные меры для этого (как в данном примере) не потребуется.
    """
    pid = os.getpid()
    print(f'starting send_signals for {pid}')

    for name in ['SIGHUP', 'SIGHUP', 'SIGUSR1', 'SIGINT']:
        print(f'sending {name}')
        os.kill(pid, getattr(signal, name))
        # Уступить управление, чтобы позволить выполняться
        # обработчику сигнала, поскльку сам по себе сигнал
        # не прерывает работу программы
        print('yielding control')
        await asyncio.sleep(0.01)
    return

if __name__ == '__main__':
    """
    Обработчики сигналов регистрируются c помощью метода add_signal_handler(). 
    Первый аргумент — это сигнал, второй — функция обратного вызова.
    Функциям обратного вызова не передаются никакие аргументы, поэтому, если 
    необходимо передавать им аргументы, их следует обертывать функцией functools.partial().
    """
    event_loop = asyncio.get_event_loop()

    event_loop.add_signal_handler(
        signal.SIGHUP,
        functools.partial(signal_handler, name='SIGHUP')
    )
    event_loop.add_signal_handler(
        signal.SIGUSR1,
        functools.partial(signal_handler, name='SIGUSR1')
    )
    event_loop.add_signal_handler(
        signal.SIGINT,
        functools.partial(signal_handler, name='SIGINT'),
    )
    try:
        event_loop.run_until_complete(send_signals())
    finally:
        event_loop.close()