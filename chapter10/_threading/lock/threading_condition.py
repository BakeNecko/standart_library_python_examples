"""
Помимо объектов Event существует другой способ синхронизации потоков:
c помощью объектов Condition. Поскольку класс Condition использует класс
Lock, объект этого типа можно связать c разделяемым ресурсом, позволяя
нескольким потокам ожидать, пока данный ресурс не будет обновлен.
В следующем примере потоки consumer () ожидают, пока не будет установлен объект
Condition, прежде чем продолжить выполнение. За установку условия и извещение
других потоков о том, что они могут продолжить выполнение, отвечает поток producer().
"""
import logging
import threading
import time


def consumer(cond: 'threading.Condition'):
    """Дождаться наступления условия и затем использовать ресурс."""
    logging.debug('Starting consumer thread')
    with cond:
        cond.wait()
        logging.debug('Resource is available to consumer')


def producer(cond: 'threading.Condition'):
    """Настроить ресурс для использования потребителем."""
    logging.debug('Starting producer thread')
    with cond:
        logging.debug('Making resource available')
        cond.notifyAll()


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s'
)

if __name__ == '__main__':
    condition = threading.Condition()
    c1 = threading.Thread(name='c1', target=consumer, args=(condition,))
    c2 = threading.Thread(name='c2', target=consumer, args=(condition,))
    p = threading.Thread(name='p', target=producer, args=(condition,))

    c1.start()
    time.sleep(0.2)
    c2.start()
    time.sleep(0.2)
    p.start()
