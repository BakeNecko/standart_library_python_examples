"""
Сигналы и потоки

Совместное использование сигналов и потоков редко работает хорошо, поскольку
получать сигналы будет только основной поток. Следующий сценарий
устанавливает обработчик сигналов, ожидает получения сигналов в одном потоке
и посылает сигнал из другого потока.

Здесь все обработчики сигналов были зарегистрированы в основном потоке,
как того требует реализация модуля signal в Python, независимо от обеспечиваемой
базовой платформой поддержки сочетания потоков и сигналов. Несмотря на
то что поток-получатель выполняет вызов signal.pause (), в действительности
он не получает сигнал. Вызов signal.alarm(2) в конце сценария предотвращает
бесконечную блокировку, обусловленную тем, что поток-получатель никогда не
вернет управление.
"""
import signal
import threading
import os
import time

print('Current thread: ', threading.current_thread().name)


def signal_handler(num, stack):
    print('Received signal {} in {}'.format(num, threading.current_thread().name))


signal.signal(signal.SIGUSR1, signal_handler)


def wait_for_signal():
    print('Waiting for signal in', threading.current_thread().name)
    signal.pause()
    print('Done waiting')


# Запустить поток который не будет получить сигналы
receiver = threading.Thread(
    target=wait_for_signal,
    name='receiver',
)
receiver.start()
time.sleep(1)


def send_signal():
    print('Sending signal in', threading.current_thread().name)
    os.kill(os.getpid(), signal.SIGUSR1)


if __name__ == '__main__':
    sender = threading.Thread(target=send_signal, name='sender')
    sender.start()
    sender.join()

    # Ожидать появления сигнала (этого никогда не произойдет)
    print('Waiting for ', receiver.name)
    signal.alarm(2)
    receiver.join()
