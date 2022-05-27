import signal
import os
import time


def receive_signal(signum, stack):
    print('Receive: ', signum)
    print('Stack: ', stack)


# Регистрация дескрипторов сигналов
signal.signal(signal.SIGUSR1, receive_signal)
signal.signal(signal.SIGUSR2, receive_signal)

# Вывод ID процесса, который впоследствии можно будет
# использовать с командой kill для отправки сигналов этой программе

if __name__ == '__main__':
    # В терминале вводим
    # kill -USR1 <pid>
    # kill -USR2 <pid>
    # kill -INT <pid>
    print('My PID is: ', os.getpid())

    while True:
        print('Waiting...')
        time.sleep(3)
