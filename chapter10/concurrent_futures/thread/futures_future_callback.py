# 10.6.4 Обратные вызовы с использованием экземпляров Future
"""
Чтобы предпринять некоторое действие по завершении задачи без явного
ожидания результата, можно указать c помощью метода add_done_callback()
другую функцию, которая должна быть вызвана, когда экземпляр Future перейдет
в состояние готовности. Функция обратного вызова должна быть вызываемым объектом,
получающим единственный аргумент: экземпляр Future.
"""
from concurrent import futures
import time


def task(n):
    print(f'{n}: sleeping')
    time.sleep(0.5)
    print(f'{n}: done')
    return n / 10


def done(fn: 'futures.Future'):
    if fn.cancelled():
        print(f'{fn.arg}: canceled')
    elif fn.done():
        error = fn.exception()
        if error:
            print('{}: error returned: {}'.format(fn.arg, error))
        else:
            result = fn.result()
            print('{}: value returned: {}'.format(
                fn.arg, result
            ))


if __name__ == '__main__':
    ex = futures.ThreadPoolExecutor(max_workers=2)
    print('main: starting')
    f = ex.submit(task, 5)
    f.arg = 5
    f.add_done_callback(done)
    result = f.result()
