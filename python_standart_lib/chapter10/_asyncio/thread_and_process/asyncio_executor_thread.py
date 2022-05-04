# 10.5.14.1 Потоки
"""
Метод run_in_executor() цикла событий получает в качестве аргументов
экземпляр executor, который обычно является вызываемым объектом (функцией),
и аргументы, которые должны быть переданы этому вызываемому объекту.
Возвращаемым значением метода run_in_executor() является экземпляр Future,
который можно использовать для ожидания завершения работы указанной функции
и возврата соответствующего значения. Если экземпляр executor не предоставляется,
то создается экземпляр ThreadPoolExecutor. В следующем примере явным образом
создается объект executor c ограниченным количеством доступных ему потоков.

Экземпляр ThreadPoolExecutor запускает свои рабочие потоки и вызывает в
каждом из них предоставленные экземпляры функции. В этом примере показано,
каким образом совместное использование методов run in_executor() и wait()
позволяет сопрограмме сначала уступать управление циклу событий, пока блокирующие
функции выполняются в отдельных потоках, а затем пробуждаться, когда эти функции
завершают свою работу.
"""
from typing import Union
import asyncio
import concurrent.futures
import logging
import sys
import time

ThreadOrProcess = Union['concurrent.futures.ThreadPoolExecutor', 'concurrent.futures.ProcessPoolExecutor']


def blocks(n):
    log = logging.getLogger(f'blocks({n})')
    log.info('running')
    time.sleep(0.1)
    log.info('done')
    return n ** 2


async def run_blocking_task(executor: ThreadOrProcess):
    log = logging.getLogger('run_blocking_task')
    log.info('starting')

    log.info('creating executor task')
    loop = asyncio.get_event_loop()
    blocking_task = [
        loop.run_in_executor(executor, blocks, i)
        for i in range(6)
    ]
    log.info('waiting for executor tasks')
    completed, pending = await asyncio.wait(blocking_task)
    results = [t.result() for t in completed]
    log.info('results: {!r}'.format(results))

    log.info('exiting')


if __name__ == '__main__':
    """
    Использование модуля logging (раздел 14.80) в сценарии asyncio_executor_thread.py 
    позволяет удобным образом проследить за тем, c каким потоком и какой функцией 
    связано каждое сообщение. Поскольку в каждом вызове blocks() используется свой 
    объект log, вывод отчетливо показывает, что одни и тс же потоки повторно 
    используются для вызова нескольких экземпляров функций c различными аргументами.
    """
    # Сконфигурировать протоколирование для отображения имени
    # потока, из которого поступило сообщение
    logging.basicConfig(
        level=logging.INFO,
        format='%(threadName)10s %(name)18s: %(message)s',
        stream=sys.stderr,
    )

    # Создть ограниченный пул потоков
    executor = concurrent.futures.ThreadPoolExecutor(
        max_workers=3,
    )

    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(
            run_blocking_task(executor)
        )
    finally:
        event_loop.close()
