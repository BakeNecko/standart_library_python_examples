"""
Несмотря на то что сигналы таймера можно установить в любом потоке, их
всегда получает основной поток
"""
import signal
import time
import threading


def signal_handler(num, stack):
    print(time.ctime(), 'Alarm in', threading.current_thread().name)


signal.signal(signal.SIGALRM, signal_handler)


def use_alarm():
    t_name = threading.current_thread().name
    print(time.ctime(), 'Setting alarm in', t_name)
    signal.alarm(1)
