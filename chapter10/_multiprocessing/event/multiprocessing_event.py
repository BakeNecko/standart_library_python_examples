# 10.4.11 Обмен сигналами меду процессами
"""
Класс Event, представляющий события, обеспечивает простой способ обмена
информацией о состоянии между процессами. Объект события может находиться
в одном из двух состояний: “установлено” и “не установлено”. Пользователи
объекта события могут дожидаться его перехода из состояния “не установлено” в
состояние “установлено”, используя необязательное значение тайм-аута.
"""
import multiprocessing
import time


def wait_for_event(_e: 'multiprocessing.Event'):
    """Дождаться события, прежде чем делать что-либо."""
    print('wait_for_event: starting')
    _e.wait()
    print('wait_for_event: e.is_set() -> ', _e.is_set())


def wait_for_event_timeout(_e, t):
    """Подождать t секунд и затем завершиться по тайм-ауту"""
    print('wait_for_event_timeout: starting')
    _e.wait(t)
    print('wait_for_event_timeout: e.is_set() -> ', _e.is_set())


if __name__ == '__main__':
    """
    По истечении тайм-аута метод wait() возвращает управление, не генерируя
    ошибку. Ответственность за проверку состояния объекта события c помощью 
    метода is_set() возлагается на вызывающий код.
    """
    e = multiprocessing.Event()
    w1 = multiprocessing.Process(
        name='block',
        target=wait_for_event,
        args=(e,),
    )
    w1.start()

    w2 = multiprocessing.Process(
        name='nonblock',
        target=wait_for_event_timeout,
        args=(e, 2),
    )
    w2.start()

    print('main: waiting before calling Event.set()')
    time.sleep(3)
    e.set()
    print('main: event is set')
