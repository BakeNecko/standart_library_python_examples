"""
Если с одним из рабочих процессов происходит нечто, что приводит к его
непредвиденному завершению, то работа экземпляра ProcessPoolExecutor
считается прерванной, и он больше не используется для планирования
выполнения задач.
"""
from concurrent import futures
import os
import signal

if __name__ == '__main__':
    """
    Фактическое возбуждение исключения BrokenProcessPool происходит при
    обработке результатов, а не при предоставлении новой задачи.
    """
    with futures.ProcessPoolExecutor(max_workers=2) as ex:
        print('getting the pid for one worker')
        f1 = ex.submit(os.getpid)
        pid1 = f1.result()

        print(f'killing process {pid1}')
        os.kill(pid1, signal.SIGHUP)

        print('submitting another task')
        f2 = ex.submit(os.getpid)
        try:
            pid2 = f2.result()
        except futures.process.BrokenProcessPool as e:
            print(f'could not start new tasks: {e}')