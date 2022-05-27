"""
Обмен сигналами между потками

Несмотря на то что цель использования нескольких потоков — параллельное
выполнение независимых операций, иногда важно синхронизировать операции,
выполняемые в двух или более потоках. Объекты событий обеспечивают простой
способ организации безопасного взаимодействия потоков. Объект Event имеет
внутренний флаг, который другие потоки могут устанавливать и сбрасывать c
помощью методов set() и clear(). C помощью метода wait() можно приостановить
работу потока до тех пор, пока другой поток не установит указанный флаг,
вызвав метод set(), или пока не истечет заданный интервал времени.

Метод wait() получает один аргумент, определяющий предельное время ожидания
события (в секундах). Возвращаемое им булево значение указывает на то,
установлен ли внутренний флаг, благодаря чему вызывающему коду становится
известно, по какой причине метод wait() вернул управление. Чтобы проверить
состояние этого флага для заданного события без риска блокировки, можно
использовать метод is_set()

В данном примере функция wait_for_event_timeout () проверяет статус события,
не создавая бесконечной блокировки. Функция wait_for_event () блокируется
на вызове метода wait (), который не возвращает управление до тех нор,
пока не изменится статус события.
"""
import logging
import threading
import time


def wait_for_event(e: 'threading.Event'):
    """Дождаться установки события, прежде чем что-то едалть."""
    logging.debug('wait_for_event starting')
    event_is_set = e.wait()
    logging.debug('event set: %s', event_is_set)


def wait_for_event_timeout(e: 'threading.Event', t):
    """Подождать t секунд и завершиться по тайм-ауту"""
    while not e.is_set():
        logging.debug('wait_for_event_timeout starting')
        event_is_set = e.wait(t)
        logging.debug('event set: %s', event_is_set)
        if event_is_set:
            logging.debug('processing event')
        else:
            logging.debug('doing other work')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s'
)
if __name__ == '__main__':
    e = threading.Event()
    t1 = threading.Thread(
        name='block',
        target=wait_for_event,
        args=(e,),
    )
    t1.start()

    t2 = threading.Thread(
        name='nonblock',
        target=wait_for_event_timeout,
        args=(e, 2),
    )
    t2.start()

    logging.debug('Waiting before calling Event.set()')
    time.sleep(0.3)
    e.set()
    logging.debug('Event is set')
