import logging
import threading
import time


def worker():
    logging.debug('Starting')
    time.sleep(0.2)
    logging.debug('Existing')


def my_service():
    logging.debug('Starting')
    time.sleep(0.3)
    logging.debug('Existing')


logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s'
)
t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker)  # Исп имя по умл

if __name__ == '__main__':
    """
    Отладочный вывод включает строки, каждая из которых содержит имя текущего потока. 
    Строкам, содержащим имя "Thread-1", соответствует неименованный поток w2.
    """
    w.start()
    w2.start()
    t.start()
