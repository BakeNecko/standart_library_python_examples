"""
Объекты Lock реализуютАР1 менеджера контекста и совместимы c инструкцией with.
Использование инструкции with устраняет необходимость в явном получении и
освобождении блокировки
"""
import threading
import logging


def worker_with(lock: threading.Lock):
    with lock:
        logging.debug('Lock acquired via with')


def worker_no_with(lock: threading.Lock):
    lock.acquire()
    try:
        logging.debug('Lock acquired directly')
    finally:
        lock.release()


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s'
)

if __name__ == '__main__':
    lock = threading.Lock()
    w = threading.Thread(target=worker_with, args=(lock,))
    nw = threading.Thread(target=worker_no_with, args=(lock,))
    w.start()
    nw.start()
