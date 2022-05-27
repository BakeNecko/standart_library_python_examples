# 10.4.9. Создание подклассов Process
"""
Использование экземпляров Process, представляющих процессы, c передачей
им целевой функции — простейший способ запуска задачи в отдельном процессе.
Однако этот способ — не единственный. Другой вариант — использовать
пользовательский подкласс.
"""
import multiprocessing


class Worker(multiprocessing.Process):

    def run(self):
        """
        Для выполнения возложенной на него работы производный
        класс должен переопределить метод run()
        """
        print('In {}'.format(self.name))
        return


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = Worker()
        jobs.append(p)
        p.start()
    for j in jobs:
        j.join()
