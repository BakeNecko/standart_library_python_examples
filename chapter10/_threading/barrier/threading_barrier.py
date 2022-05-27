"""
Еще одним механизмом синхронизации являются барьеры. Объект Barrier
создает контрольную точку для заданного количества потоков, каждый из которых,
достигнув контрольной точки, блокируется до тех пор, пока ее не достигнут
все потоки, участвующие в этом механизме блокировки. При таком подходе потоки
могут запускаться по отдельности, а затем переходить в состояние ожидания
до тех пор, пока все они не будут готовы к продолжению выполнения.

В этом примере объект Barrier конфигурируется для блокирования потоков
в контрольной точке до тех пор, пока все три потока не перейдут в состояние
ожидания. Как только это условие выполняется, все три потока освобождаются
одновременно. Значение, возвращаемое методом wait(), указывает на количество
освобожденных процессов-участников и может использоваться для наложения
ограничений на выполнение потоками таких действий, как освобождение
совместно используемого ресурса

Barrier(parties, action=None, timeout=None)
-------------------------------------------
Класс Barrier() модуля threading создает объект-барьер для количества parties потоков.
Аргумент action, если он предусмотрен, вызывается одним из потоков при их освобождении.
Аргумент timeout - это значение тайм-аута по умолчанию, если он не указан для метода Barrier.wait().

Каждый из потоков пытается преодолеть барьер, вызывая метод Barrier.wait(),
и будет блокироваться, пока все потоки не выполнят свои вызовы Barrier.wait()
Как только все потоки выполнили свои вызовы, то в этот момент потоки освобождаются одновременно.
"""
import threading
import time


def worker(barrier: 'threading.Barrier'):
    print(
        threading.current_thread().name,
        # n_waiting количество потоков, ждущих прохождения барьера
        f'waiting for barrier with {barrier.n_waiting} others\n'
    )
    worker_id = barrier.wait()
    print(threading.current_thread().name, ' after barrier ', worker_id, '\n')


NUM_THREADS = 3

if __name__ == '__main__':
    barrier = threading.Barrier(NUM_THREADS)
    threads = [
        threading.Thread(
            name='worker-%s' % i,
            target=worker,
            args=(barrier,),
        )
        for i in range(NUM_THREADS)
    ]
    for t in threads:
        print(t.name, 'starting')
        t.start()
        time.sleep(0.1)

    for t in threads:
        t.join()
