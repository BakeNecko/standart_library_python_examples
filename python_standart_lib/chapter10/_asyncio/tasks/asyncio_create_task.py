# 10.5.5.1 Запуск задачи
"""
Чтобы запустить задачу, следует создать экземпляр Task, используя метод
create_task(). Результирующая задача будет выполняться как часть параллельных
операций, управляемых циклом событий, до тех пор пока выполняется цикл и сопрограмма
не возвращает управление.
"""
import asyncio


async def task_func():
    print('in task_func')
    return 'the result'


async def main(loop):
    print('creating task')
    task = loop.create_task(task_func())
    print('waiting for {!r}'.format(task))
    return_value = await task
    print('task completed {!r}'.format(task))
    print('return value: {!r}'.format(return_value))

if __name__ == '__main__':
    """
    В этом примере функция main() ожидает возврата результата задачей, после
    чего возвращает управление.
    """
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main(event_loop))
    finally:
        event_loop.close()