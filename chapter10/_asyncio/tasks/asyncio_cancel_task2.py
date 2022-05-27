"""
Если задача отменяется в то время, когда она ожидает завершения другой
параллельной операции, она извещается об этом возбуждением исключения
CancelledError в точке ожидания.
"""
import asyncio


async def task_func():
    print('in task_func, sleeping')
    try:
        await asyncio.sleep(1)
    except asyncio.CancelledError:
        print('task_func was canceled')
        raise
    return 'the result'


def task_canceler(t: 'asyncio.Task'):
    print('in task_canceller')
    t.cancel()
    print('canceled the task')


async def main(loop: 'asyncio.AbstractEventLoop'):
    print('creating task')
    task = loop.create_task(task_func())
    loop.call_soon(task_canceler, task)

    try:
        await task
    except asyncio.CancelledError:
        print('main() also sees task as canceled')


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main(event_loop))
    finally:
        print('close event_loop')
        event_loop.close()
