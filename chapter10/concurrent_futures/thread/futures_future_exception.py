# 10.6.6 Возбуждение исключений в задах
"""
Если задача генерирует необрабатываемое исключение, то оно сохраняется в
экземпляре Future для данной задачи и становится доступным через вызов
метода result() или exception().
"""
from concurrent import futures


def task(n):
    print('{}: starting'.format(n))
    raise ValueError('the value {} is not good'.format(n))


if __name__ == '__main__':
    """
    Если метод result() вызывается после возбуждения необрабатываемого исключения 
    в функции задачи, то же самое исключение возбуждается в текущем контексте.
    """
    ex = futures.ThreadPoolExecutor(max_workers=2)
    print('main: strting')
    f = ex.submit(task, 5)

    error = f.exception()
    print(f'main: error: {error}')

    try:
        result = f.result()
    except ValueError as e:
        print(f'main: saw error "{e}" when accessing result')
