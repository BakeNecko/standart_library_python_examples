# 10.4.14 Контроль одновременноо доступа к ресурсам
"""
Иногда полезно разрешить нескольким рабочим процессам одновременный
доступ к одному и тому же ресурсу, но при этом ограничить общее количество
процессов, которым предоставляется такая возможность. В качестве примера
можно привести пул, поддерживающий фиксированное количество соединений,
или сетевое приложение, поддерживающее фиксированное количество
одновременных загрузок. Одним из способов управления подобными
соединениями являются семафоры, представляемые классом Semaphore.
"""
import random
import multiprocessing
import time


class ActivePool:

    def __init__(self):
        super(ActivePool, self).__init__()
        self.mgr = multiprocessing.Manager()
        self.active = self.mgr.list()
        self.lock = multiprocessing.Lock()

    def makeActive(self, name):
        with self.lock:
            self.active.append(name)

    def makeInactive(self, name):
        with self.lock:
            self.active.remove(name)

    def __str__(self):
        with self.lock:
            return str(self.active)


def worker(s: 'multiprocessing.Semaphore', pool: 'ActivePool'):
    name = multiprocessing.current_process().name
    with s:
        pool.makeActive(name)
        print(f'Activation {name} now running {pool}')
        time.sleep(random.random())
        pool.makeInactive(name)


if __name__ == '__main__':
    """
    В этом примере в качестве удобного средства, позволяющего отслеживать
    процессы, выполняющиеся в заданный момент времени, используется класс
    ActivePool. Вероятно, при работе c реальным пулом такие ресурсы, как 
    соединения, распределялись бы между активными процессами и возвращались в пул
    по завершении выполнения задачи. В данном случае пул используется всего лишь
    для хранения имен активных процессов и демонстрации того факта, что только
    три процесса выполняются одновременно.
    """
    pool = ActivePool()
    s = multiprocessing.Semaphore(3)
    jobs = [
        multiprocessing.Process(
            target=worker,
            name=str(i),
            args=(s, pool),
        )
        for i in range(10)
    ]
    for j in jobs:
        j.start()

    while True:
        alive = 0
        for j in jobs:
            if j.is_alive():
                alive += 1
                j.join(timeout=0.1)
                print(f'Now running {pool}')
        if alive == 0:
            # все задачи выполненны
            break
