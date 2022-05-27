# 10.6.1 Использование метода map() с базовым пулом потоков
"""
Класс ThreadPoolExecutor управляет набором рабочих потоков, передавая
им задачи по мере того, как они освобождаются для выполнения очередной
порции работы. В следующем примере c помощью метода map() организуется
получение набора результатов параллельной обработки входного итерируемого
объекта. C помощью метода time.sleep() в задачах создаются паузы различной
длительности, чтобы продемонстрировать, что метод map() всегда возвращает
результаты в соответствии с порядком поступления входных данных, независимо
от порядка завершения параллельных задач.
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
    """
    Возвращаемое методом map () значение в действительности является специальным 
    типом итератора, которому известно, как следуетдожидаться очередного ответа 
    по мере того, как основная программа выполняет итерации по нему.
    """
    ex = futures.ThreadPoolExecutor(max_workers=2)
    print('main: strting')
    results = ex.map(task, range(5, 0, -1))
    print(f'main: unprocessed results {results}')
    print('main: waiting for real results')
    real_results = list(results)
    print(f'main: results: {real_results}')
