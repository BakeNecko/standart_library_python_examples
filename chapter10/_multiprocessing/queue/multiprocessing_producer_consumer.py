"""
Ниже приведен более сложный пример управления несколькими рабочими
процессами, которые получают данные из очереди JoinableQueue и возвращают
результаты родительскому процессу. Для принудительного завершения рабочих
процессов используется метод “отравленной таблетки”. После настройки реальных
задач основная программа добавляет в очередь по одному “стоп-значению” на
рабочий процесс. Когда рабочему процессу встречается это специальное значение,
он выходит из своего цикла обработки. Основной процесс использует метод join()
очереди задач для того, чтобы организовать ожидание завершения всех задач,
прежде чем обработать результаты
"""
import multiprocessing
import os
import time


class Consumer(multiprocessing.Process):
    def __init__(self,
                 task_queue: 'multiprocessing.JoinableQueue[Task]',
                 result_queue: 'multiprocessing.Queue'):
        super(Consumer, self).__init__()
        self.task_queue = task_queue
        self.result_queue = result_queue

    def run(self):
        proc_name = self.name
        while True:
            next_task = self.task_queue.get()
            if next_task is None:
                # Прекращение выполнения с помощью "отравленной таблетки"
                print(f'{proc_name}: Exiting')
                self.task_queue.task_done()
                break
            print(f'{proc_name}: {next_task}')
            answer = next_task()
            self.task_queue.task_done()
            self.result_queue.put(answer)


class Task:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        time.sleep(0.1)  # имитация выполнения работы
        return f'{self.a} * {self.b} = {self.a * self.b}'

    def __str__(self):
        return f'{self.a} * {self.b}'


if __name__ == '__main__':
    # Создание очередей обмена сообщениями
    tasks = multiprocessing.JoinableQueue()
    result = multiprocessing.Queue()

    # Запуск потребителей
    num_consumers = os.cpu_count() * 2
    print(f'Creating {num_consumers} consumers')
    consumers = [
        Consumer(tasks, result)
        for i in range(num_consumers)
    ]
    for w in consumers:
        w.start()

    # Помещение задач в очередь
    num_jobs = 10
    for i in range(num_jobs):
        tasks.put(Task(i, i))

    # Добавление отравленной таблетки для каждого потребителя
    for i in range(num_consumers):
        tasks.put(None)

    # Ожидание завершения всех задач
    tasks.join()
    while num_jobs:
        print('Result: ', result.get())
        num_jobs -= 1
