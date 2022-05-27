# 10.5.5.2 Отмена выполнения задачи
"""
Сохранив объект Task, возвращенный методом create_task(), можно отме­
нить выполнение задачи до ее завершения.
"""
import asyncio


async def task_func():
    print('in task_func')
    return 'the result'


async def main(loop):
    print('creating task')
    task = loop.create_task(task_func())

    print('canceling task')
    task.cancel()

    print('canceled task {!r}'.format(task))
    try:
        await task
    except asyncio.CancelledError:
        print('caught error from canceled task')
    else:
        print('task result: {!r}'.format(task.result()))

if __name__ == '__main__':
    """
    В этом примере выполнение предварительно созданной задачи отменяется до
    запуска цикла событий. Вследствие этого метод run_until__complete() 
    возбуждает исключение CancelledError.
    """
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main(event_loop))
    finally:
        event_loop.close()