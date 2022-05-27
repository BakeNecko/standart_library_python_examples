"""
Чтобы игнорировать сигнал, следует зарегистрировать SIG_IGN в качестве обработчика.
В следующем сценарии обработчик по умолчанию для сигнала SIGINT заменяется на SIG_IGN
и устанавливается обработчикдля сигнала SIGUSR1. После этого вызов signal.pause()
переводит программу в состояние ожидания до получения сигнала.
"""
import signal
import os
import time


def do_exit(sig, stack):
    raise SystemExit('Exiting')


signal.signal(signal.SIGINT, signal.SIG_IGN)
signal.signal(signal.SIGUSR1, do_exit)

print('My PID:', os.getpid())

if __name__ == '__main__':
    """
    Обычно сигнал SIGINT (сигнал, посылаемый программе командной оболочкой 
    при нажатии пользователем комбинации клавиш <Ctrl+C) возбуждает исключение 
    KeyboardInterrupt. В этом примере сигнал SIGINT игнорируется, а при
    получении сигнала SIGUSR1 возбуждается исключение SystemExit. Каждое появление 
    символов ЛС в выводе означает, что пользователь предпринимал попытку
    прервать выполнение сценария нажатием комбинации клавиш <Ctrl+C> на консоли. 
    Чтобы завершить выполнение сценария, следует выполнить на другом терми-
    налекоманду kill -USR1 <pid>.
    """
    signal.pause()
