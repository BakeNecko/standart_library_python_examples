"""
Для инициализации параметров таким образом, чтобы все потоки запускались с одним
и тем же значением, можно использовать подкласс и установить атрибуты в методе __init__().
"""

import random
import threading
import logging


def show_value(data):
    try:
        val = data.value
    except AttributeError:
        logging.debug('No value yet')
    else:
        logging.debug(f'value={val}')


def worker(data):
    show_value(data)
    data.value = random.randint(1, 100)
    show_value(data)


class MyLocal(threading.local):
    def __init__(self, value):
        super().__init__()
        logging.debug('Initializing %r', self)
        self.value = value


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

if __name__ == '__main__':
    # Значения по умолчанию устанавливаются посредством вызова метода
    # init__ () для одного и того же объекта (обратите внимание на значение id ()) по
    # одному разу в каждом потоке
    local_data = MyLocal(1000)
    show_value(local_data)

    for i in range(2):
        t = threading.Thread(target=worker, args=(local_data,))
        t.start()
