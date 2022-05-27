# 10.6.2 Планирование индивидуальных задач
"""
Помимо метода map() существует еще одна возможность планировать выполнение
индивидуальных задач с помощью объекта-исполнителя, используя метод submit().
Возвращаемый им экземпляр Future может быть далее использован
для ожидания результатов выполнения конкретной задачи.
"""
from concurrent import futures
import threading
import time


def task(n):
    print('{}: sleeping {}'.format(
        threading.current_thread().name, n
    ))
    time.sleep(n / 10)
    print('{}: done with {}'.format(
        threading.current_thread().name, n
    ))
    return n / 10


if __name__ == '__main__':
    ex = futures.ThreadPoolExecutor(max_workers=2)
    print('main: strting')
    f = ex.submit(task, 5)
    print(f'main: future: {f}')
    print('main: waiting for results')
    results = f.result()
    print(f'main: results: {results}')
    print(f'main: future after result: {f}')
