# 10.4.3 Определение текущего процесса
"""
Передача аргумента для идентификации процесса или присвоения ему имени
— это хлопоты, от которых можно избавиться. Каждый экземпляр Process
получает имя по умолчанию, которое можно изменить при создании ггроцесса.
Именование процессов удобно для их отслеживания, особенно в приложениях, в
которых одновременно выполняется несколько различных типов процессов.
"""
import multiprocessing
import time


def worker():
    name = multiprocessing.current_process().name
    print(name, 'starting')
    time.sleep(2)
    print(name, 'Exiting')


def my_service():
    name = multiprocessing.current_process().name
    print(name, 'starting')
    time.sleep(3)
    print(name, 'Exiting')


if __name__ == '__main__':
    service = multiprocessing.Process(
        name='my_service',
        target=my_service,
    )
    worker_1 = multiprocessing.Process(
        name='worker_1',
        target=worker
    )
    worker_2 = multiprocessing.Process(
        target=worker
    )
    worker_1.start()
    worker_2.start()
    service.start()