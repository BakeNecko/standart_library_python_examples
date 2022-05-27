"""
Простейший способ использования класса Thread — это его инстанциализа-
ция c указанием целевой функции и вызов метода start(), запускающего поток.
"""
import threading


def worker(num):
    """Функция рабочего потока"""
    print(f'Worker {num}')


threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()
