# 10.5.5.3 Создание задач из сопрограмм
"""
Функция ensure_future () возвращает экземпляр Task, связанный c выполннием
сопрограммы. Этот экземпляр можно передать другому коду, который будет ожидать
его завершения, не зная, каким образом была сконструирована или вызвана сопрограмма.
"""
import asyncio
import sys


async def wrapped():
    print('wrapped')
    return 'result'


async def inner(task: 'asyncio.Task'):
    print('inner: starting')
    print('inner: waiting for {!r}'.format(task))
    result = task.result()
    print('inner: task returned {!r}'.format(result))


async def starter():
    print('starter: creating task')
    task = asyncio.ensure_future(wrapped())
    print('starter: waiting for inner')
    print('sleeping...')
    await asyncio.sleep(3)
    await inner(task)
    print('starter: inner returned')


if __name__ == '__main__':
    """
    Обратите внимание на то, что сопрограмма, переданная функции ensure_future(), 
    не запустится до тех пор, пока где-нибудь не будет использовано 
    ключевое слово await, разрешающее ее выполнение
    P.S судя по asyncio.sleep(2) это не так. Сопрограмма выполняется сразу? 
    """
    event_loop = asyncio.get_event_loop()
    try:
        print('entering event loop')
        result = event_loop.run_until_complete(starter())
    finally:
        event_loop.close()
