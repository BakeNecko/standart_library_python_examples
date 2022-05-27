# 10.6.8 Пулы процессов
"""
Экземпляры ProcessPoolExecutor работают аналогичноэкземплярам Thread
7oolExecutor, ио используют процессы вместо потоков. Этот подход позволяет
интенсивным вычислительным операциям использовать отдельные CPU,
не подвергаясь глобальной блокировке интерпретатора CPython
"""
from concurrent import futures
import os


def task(n):
    return n, os.getpid()


if __name__ == '__main__':
    """
    Как и в случае пула потоков, отдельные рабочие процессы повторно 
    используются для выполнения множества задач.
    """
    ex = futures.ProcessPoolExecutor(max_workers=2)
    results = ex.map(task, range(5, 0, -1))
    for n, pid in results:
        print(f'ran task {n} in process {pid}')
