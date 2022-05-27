"""
В этом примере класс ActivePool обеспечивает удобный способ отслеживания
потоков, способных выполняться в данный момент. Вероятно, при работе
з реальным пулом ресурсов он распределял бы соединения или другие значения
иежду активными потоками и возвращал их в пул по завершении потока. В данном
случае пул используется всего лишь для хранения имен активных потоков и
демонстрации того факта, что одновременно выполняется не более двух потоков.
"""
import logging
import threading
import time


class ActivePool:

    def __init__(self):
        super(ActivePool, self).__init__()
        self.active = []
        self.lock = threading.Lock()

    def make_active(self, name):
        with self.lock:
            self.active.append(name)
            logging.debug(f'Running: {self.active}')

    def make_inactive(self, name):
        with self.lock:
            self.active.remove(name)
            logging.debug(f'Running: {self.active}')


def worker(s: 'threading.Semaphore', pool: 'ActivePool'):
    logging.debug('Waiting to join the pool')
    with s:  # Одновременно не работает более 2х потоков
        name = threading.current_thread().getName()
        pool.make_active(name)
        time.sleep(0.1)
        pool.make_inactive(name)


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s (%(threadName)-2s) %(message)s'
)

if __name__ == '__main__':
    pool = ActivePool()
    s = threading.Semaphore(2)
    for i in range(4):
        t = threading.Thread(
            target=worker,
            name=str(i),
            args=(s, pool),
        )
        t.start()
