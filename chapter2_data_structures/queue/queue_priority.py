"""
Класс PriorityQueue
использует упорядочение очереди по приоритетам для принятия решения
относительно того, какой из элементов следует извлечь.
"""
import functools
import queue
import threading


@functools.total_ordering
class Job:

    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print('New job:', description)
        return

    def __eq__(self, other: 'Job'):
        try:
            return self.priority == other.priority
        except AttributeError:
            return NotImplemented

    def __lt__(self, other: 'Job'):
        try:
            return self.priority < other.priority
        except AttributeError:
            return NotImplemented


if __name__ == '__main__':
    q = queue.PriorityQueue()
    q.put(Job(3, 'Mid-level job'))
    q.put(Job(3, 'Mid-level job'))
    q.put(Job(10, 'Low-level job'))
    q.put(Job(10, 'Low-level job'))
    q.put(Job(10, 'Low-level job'))
    q.put(Job(1, 'Important job'))
    q.put(Job(1, 'Important job'))


    def process_job(q):
        while True:
            next_job = q.get()
            print('Processing job:', next_job.description)
            q.task_done()


    workers = [
        threading.Thread(target=process_job, args=(q,)),
        threading.Thread(target=process_job, args=(q,)),
    ]
    for w in workers:
        w.setDaemon(True)
        w.start()
    q.join()
