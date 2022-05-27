"""
Перечисление всех потоков

Чтобы обеспечить завершение всех потоков-демонов прежде, чем завершится
эсновной поток, вовсе не обязательно хранить явные дескрипторы каждого из
яих. Метод enumerate() возвращает список всех активных экземпляров Thread.
Поскольку основной поток входит в этот список, то его присоединение к текущему
потоку c помощью метода join() создало бы ситуацию взаимоблокировки,
так что он должен быть исключен.
"""
import random
import threading
import time
import logging


def worker():
    pause = random.randint(1, 5) / 10
    logging.debug('sleeping %0.2f', pause)
    time.sleep(pause)
    logging.debug('ending')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s'
)

if __name__ == '__main__':
    for i in range(3):
        t = threading.Thread(target=worker, daemon=True)
        t.start()

    main_thread = threading.main_thread()
    for t in threading.enumerate():
        if t is main_thread:
            continue
        logging.debug('joining %s', t.getName())
        t.join()
