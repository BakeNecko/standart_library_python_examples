# 10.4.16 Разделяемы пространства имен
"""
Кроме словарей и списков класс Manager позволяет создавать разделяемые
пространства имён. Любое именованное значение, добавляемое в пространство имен,
становится видимым для всех клиентов, получающих экземпляр Namespace.
"""
import multiprocessing
import time


def producer(ns, _event):
    ns.value = 'This is the value'
    _event.set()


def consumer(ns, _event):
    try:
        print(f'Before event: {ns.value}')
    except Exception as err:
        print('Before event, error:', str(err))
    _event.wait()
    print('After event: ', ns.value)


if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    namespace = mgr.Namespace()
    event = multiprocessing.Event()
    p = multiprocessing.Process(
        target=producer,
        args=(namespace, event),
    )
    c = multiprocessing.Process(
        target=consumer,
        args=(namespace, event),
    )
    c.start()
    time.sleep(0.3)
    p.start()

    c.join()
    p.join()
