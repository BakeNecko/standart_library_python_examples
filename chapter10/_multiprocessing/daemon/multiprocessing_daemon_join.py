"""
Чтобы дождаться завершения процесса, следует использовать метод join().
"""
import multiprocessing
import time
import sys


def daemon():
    name = multiprocessing.current_process().name
    print('Starting:', name)
    time.sleep(2)
    print('Existing: ', name)


def non_daemon():
    name = multiprocessing.current_process().name
    print('Starting: ', name)
    print('Existing: ', name)


if __name__ == '__main__':
    """
    По умолчанию метод join() создаст бесконечную блокировку. Передача ему
    аргумента timeout (число c плавающей точкой) позволяет определить предельную 
    длительность периода ожидания (тайм-аут) в секундах. Если процесс не завершается 
    в течение отведенного ему времени, то метод join() возвращает
    управление
    """
    d = multiprocessing.Process(
        name='daemon',
        target=daemon,
        daemon=True
    )

    n = multiprocessing.Process(
        name='non-daemon',
        target=non_daemon,
        daemon=False,
    )
    d.start()
    n.start()

    d.join(1) # 1 is timeout
    print('d.is_alive(): ', d.is_alive())
    n.join()
