"""
По умолчанию выход из основной программы осуществляется лишь после
того, как завершатся все дочерние процессы. Но иногда запускаются фоновые
процессы, которые выполняются, не блокируя выход из основной программы,
что, например, может быть полезным в случае служб, которым непросто прервать
выполнение рабочего процесса, или же когда прерывание процесса посреди
выполняемой им задачи не может привести к потере или повреждению ценных
данных (например, в случае задачи, генерирующей контрольные сигналы для
средств мониторинга службы).
"""
import multiprocessing
import time
import sys


def daemon():
    p = multiprocessing.current_process()
    print('Starting:', p.name, p.pid)
    sys.stdout.flush()
    time.sleep(2)
    print('Existing: ', p.name, p.pid)
    sys.stdout.flush()


def non_daemon():
    p = multiprocessing.current_process()
    print('Starting: ', p.name, p.pid)
    sys.stdout.flush()
    print('Existing: ', p.name, p.pid)
    sys.stdout.flush()


if __name__ == '__main__':
    """
    Выполнение процесса-демона автоматически прекращается перед выходом
    из программы, что позволяет избежать ситуаций, в которых после завершения
    основной программы в памяти остаются процессы-сироты. Такой характер 
    поведения можно проконтролировать, выведя идентификатор процесса во время
    выполнения программы, а затем проверив список выполняющихся процессов c
    помощью команды ps.
    """
    d = multiprocessing.Process(
        name='daemon',
        target=daemon,
        daemon=True
    )
    n = multiprocessing.Process(
        name='non-daemon',
        target=non_daemon,
        daemon=False,
    )
    d.start()
    time.sleep(1)
    n.start()
