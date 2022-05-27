# 10.4.10 Передача сообщений процессам
"""
Как и в случае потоков, многопроцессная обработка чаще всего применяется
для распределения задачи между несколькими рабочими процессами,
выполняющимися параллельно. Как правило, эффективная реализация такого подхода,
предполагающего разделение работы и аккумуляцию результатов, требует организации
межпроцессного взаимодействия. Наиболее простым способом организации
взаимодействия процессов в условиях многопроцессной обработки является
двухсторонний обмен сообщениями c помощью объекта очереди Queue. Очередь
можно использовать для передачи любого объекта, сериализуемого средствами
модуля pickle (раздел 7.1)
"""
import multiprocessing


class MyFancyClass:
    def __init__(self, name):
        self.name = name

    def do_something(self):
        proc_name = multiprocessing.current_process().name
        print(f'Doing somethid fance in {proc_name} for {self.name}')


def worker(q: 'multiprocessing.Queue[MyFancyClass]'):
    obj = q.get()
    obj.do_something()


if __name__ == '__main__':
    """
    В этом коротком примере сообщение передается только одному процессу, 
    осле чего основной процесс ожидает, пока рабочий процесс завершит свою работу.
    """
    queue = multiprocessing.Queue()
    p = multiprocessing.Process(target=worker, args=(queue,))
    p.start()

    queue.put(MyFancyClass('Fancy Dan'))

    # Ждать звершения раб. процесса
    queue.close()
    queue.join_thread()
    p.join()
