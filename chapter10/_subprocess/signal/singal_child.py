import os
import signal
import time
import sys

pid = os.getpid()
received = False


def signal_usrl(signum, frame):
    """Обратный вызов, запускаемый при получении сигнала"""
    global recived
    recived = True
    print('CHILD {:>6}: Received USRL'.format(pid))
    sys.stdout.flush()


if __name__ == '__main__':
    print('Child {:>6}: Setting up signal handler'.format(pid))
    sys.stdout.flush()
    signal.signal(signal.SIGUSR1, signal_usrl)
    print('CHILD {:>6}: Pausing to wait for signal'.format(pid))
    sys.stdout.flush()
    time.sleep(3)

    if not received:
        print('CHILD {:>6}: Never received signal'.format(pid))
