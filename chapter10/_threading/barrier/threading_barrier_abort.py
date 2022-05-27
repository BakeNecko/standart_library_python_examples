"""
Вызов метода abort () объекта Barrier генерирует во всех ожидающих потоках
исключение BrokenBarrierError. Благодаря этому потоки получают возможность
выполнить завершающие операции по освобождению ресурсов, если их работа
была прервана в то время, когда они были заблокированы вызовом wait ().
"""
import threading
import time


def worker(barrier: 'threading.Barrier'):
    print(threading.current_thread().name,
          f'waiting for barrier with {barrier.n_waiting} others')
    try:
        worker_id = barrier.wait()
    except threading.BrokenBarrierError:
        print(threading.current_thread().name, 'aborting\n')
    else:
        print(threading.current_thread().name, 'after barrier', worker_id)


NUM_THREADS = 3

barrier = threading.Barrier(NUM_THREADS + 1)

threads = [
    threading.Thread(
        name=f'worker-{i}',
        target=worker,
        args=(barrier,),
    )
    for i in range(NUM_THREADS)
]

if __name__ == '__main__':
    for t in threads:
        print(t.name, 'starting')
        t.start()
        time.sleep(0.1)

    barrier.abort()

    for t in threads:
        t.join()
