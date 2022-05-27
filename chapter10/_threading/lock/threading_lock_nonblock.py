"""
Чтобы определить, получил ли другой поток блокировку, не останавливая текущий
поток, следует передать методу acquire () значение False в качестве аргумента.
В следующем примере функция worker () пытается запросить блокировку три раза
и подсчитывает количество таких попыток. В это время функция lock_holder(),
используя цикл, периодически захватывает и освобождает блокировку, делая короткие
паузы в каждом из состояний для имитации процесса загрузки данных.
"""
import logging
import threading
import time
import sys


def lock_holder(lock: 'threading.Lock'):
    logging.debug('Starting')
    while True:
        lock.acquire()
        try:
            logging.debug('Holding')
            time.sleep(0.5)
        finally:
            logging.debug('Not holding')
            lock.release()
        time.sleep(0.5)


def worker(lock: 'threading.Lock'):
    logging.debug('Starting')
    num_tries = 0
    num_acquires = 0
    while num_acquires < 3:
        time.sleep(0.5)
        logging.debug('Trying to asquire')
        have_it = lock.acquire(False)
        try:
            num_tries += 1
            if have_it:
                logging.debug('Iteration %d: Acquired', num_tries)
                num_acquires += 1
            else:
                logging.debug('Iteration %d: Not acquired', num_tries)
        finally:
            if have_it:
                lock.release()
    logging.debug('Done after %d iterations', num_tries)


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s'
)

if __name__ == '__main__':
    lock = threading.Lock()
    holder = threading.Thread(
        target=lock_holder,
        args=(lock,),
        name='LockHolder',
        daemon=True
    )
    holder.start()

    worker = threading.Thread(
        target=worker,
        args=(lock,),
        name='Worker',
    )
    worker.start()
