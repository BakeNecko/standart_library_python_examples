"""
Прежде всего объект Thread выполняет некоторые базовые операции инициализации,
а затем вызывает метод run (), который, в свою очередь, вызывает целевую
функцию, переданную конструктору. Создание подкласса Thread сводится к
переопределению метода run () для выполнения любых необходимых действий.
"""
import threading
import logging


class MyThreadWithArgs(threading.Thread):

    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name, daemon=daemon)
        self.args = args
        self.kwargs = kwargs

    def run(self):
        logging.debug('runing with %s and %s', self.args, self.kwargs)


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s'
)

if __name__ == '__main__':
    for i in range(5):
        t = MyThreadWithArgs(args=(i,), kwargs={'a': 'A', 'b': 'B'})
        t.start()
