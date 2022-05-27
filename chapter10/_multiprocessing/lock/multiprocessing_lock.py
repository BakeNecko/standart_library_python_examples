# 10.4.12 Управление доступом к ресурсам
"""
Чтобы избежать конфликтов доступа к ресурсу, разделяемому несколькими
процессами, можно использовать экземпляр класса Lock.
"""
import multiprocessing
import sys


def worker_with(lock: 'multiprocessing.Lock', stream):
    with lock:
        stream.write('Lock acquired via with\n')


def worker_no_with(lock: 'multiprocessing.Lock', stream):
    lock.acquire()
    try:
        stream.write('Lock acquired directly\n')
    finally:
        lock.release()


if __name__ == '__main__':
    """
    Если бы в этом примере оба процесса не синхронизировали свой доступ к 
    потоку вывода c помощью блокировки, то их сообщения, выводимые на консоль,
    могли бы перемежаться
    """
    lock = multiprocessing.Lock()
    w = multiprocessing.Process(
        target=worker_with,
        args=(lock, sys.stdout),
    )
    nw = multiprocessing.Process(
        target=worker_no_with,
        args=(lock, sys.stdout),
    )
    w.start()
    nw.start()

    w.join()
    nw.join()
