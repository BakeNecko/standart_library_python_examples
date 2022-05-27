# 10.6.5 Отмены выполнения задач
"""
Действие экземпляра Future можно отменить, если он был предоставлен, но
не запущен, вызвав его метод cancel().
"""
from concurrent import futures
import time


def task(n):
    print('{}: sleeping'.format(n))
    time.sleep(0.5)
    print('{}: done'.format(n))
    return n / 10


def done(fn: 'futures.Future'):
    if fn.cancelled():
        print(f'{fn.arg}: canceled')
    elif fn.done():
        print(f'{fn.arg}: not canceled')


if __name__ == '__main__':
    # Метод cancel () возвращает булево значение, указывающее на то, была ли задача отменена
    ex = futures.ThreadPoolExecutor(max_workers=2)
    print('main:  starting')
    tasks = []

    for i in range(10, 0, -1):
        print(f'main: submitting {i}')
        f = ex.submit(task, i)
        f.arg = i
        f.add_done_callback(done)
        tasks.append((i, f))
    for i, t in reversed(tasks):
        if not t.cancel():
            print(f'main: did not cancel {i}')
    ex.shutdown()
