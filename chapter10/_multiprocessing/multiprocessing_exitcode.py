# 10.4.7 Код завершения процесса
"""
Код завершения процесса доступен через атрибудет exitcode.
Диапозон его возм. значений:
== 0 | Без ошибок
> 0 | В процессе возникла ошибка, и он завершился с данным кодом
< 0 | Выполнение процесса было принудительно прекращено с помощью сигнала -1 * код_звершения
"""
import multiprocessing
import sys
import time


def exit_error():
    sys.exit(1)


def exit_ok():
    return


def return_value():
    return 1


def raises():
    raise RuntimeError('there was an error!')


def terminated():
    time.sleep(3)


if __name__ == '__main__':
    # Процессы, в которых возникло исключение, автоматически получают код завершения 1
    jobs = []
    funcs = [
        exit_error,
        exit_ok,
        return_value,
        raises,
        terminated,
    ]
    for f in funcs:
        print('Starting process for', f.__name__)
        j = multiprocessing.Process(target=f, name=f.__name__)
        jobs.append(j)
        j.start()
    jobs[-1].terminate()
    for j in jobs:
        j.join()
        print('{:>15}.exitcode = {}'.format(j.name, j.exitcode))
