"""
Потоки Timer

Один из примеров, объясняющих причину того, почему приходится создавать
подкласс Thread, предоставляет класс Timer, также содержащийся в модуле
threading. Объект Timer начинает работать c некоторой задержкой, и его можно
отменить в любой момент периода задержки.
"""
import threading
import time
import logging


def delayed():
    logging.debug('worker running')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s'
)

if __name__ == '__main__':
    t1 = threading.Timer(0.3, delayed)
    t1.setName('t1')
    t2 = threading.Timer(0.3, delayed)
    t2.setName('t2')

    logging.debug('starting timers')
    t1.start()
    t2.start()

    logging.debug('waiting before canceling %s', t2.getName())
    time.sleep(0.2)
    logging.debug('canceling %s', t2.getName())
    t2.cancel()
    logging.debug('done')
