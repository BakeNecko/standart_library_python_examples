"""
Обновление содержимого изменяемых значений в пространстве имен не
распространяется автоматически, как показано в следующем примере.
"""
import multiprocessing


def producer(ns, _event):
    # НЕ ОБНОВЛЯТЬ ГЛАБАЛЬНОЕ ЗНАЧЕНИЕ!
    ns.my_list.append('This is the value')
    _event.set()


def consumer(ns, _event):
    print('Before event: ', ns.my_list)
    _event.wait()
    print('After event :', ns.my_list)


if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    namespace = mgr.Namespace()
    namespace.my_list = []  # mgr.list() будет сохр знаечения

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
    p.start()

    c.join()
    p.join()
