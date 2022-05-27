"""
Обычные объекты блокировки типа Lock не могут быть получены более одного
раза даже одним и тем же потоком. Получение блокировки более чем одной
функцией в одной и той же цепочке вызовов может породить нежелательные
побочные эффекты.

В сигуациях, когда другой код в том же потоке должен повторно получить
блокировку, следует использовать объект RLock.
"""
import threading

if __name__ == '__main__':
    # lock = threading.Lock()
    # print('First try :', lock.acquire())
    # print('Second try :', lock.acquire(False))  # -> False
    lock = threading.RLock()
    print('First try :', lock.acquire())
    print('Second try :', lock.acquire(False))  # -> True
