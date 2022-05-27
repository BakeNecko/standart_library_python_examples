"""
В то время как одни ресурсы должны блокироваться, чтобы их могли использовать
несколько потоков, защита других должна быть организована таким образом,
чтобы они скрывались от потоков, которые не владеют ими. Конструктор local()
создает объект, способный скрывать значения от отдельных потоков.

Т.е каждый поток будет иметь свою область видимости объекта local,
даже если мы передаём тот же объект.
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


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

if __name__ == '__main__':
    # Атрибут local_data.value отсутствует в любом потоке до тех пор, пока этот
    # поток не установит его.
    local_data = threading.local()
    show_value(local_data)
    local_data.value = 1000
    show_value(local_data)

    for i in range(2):
        t = threading.Thread(target=worker, args=(local_data,))
        t.start()
