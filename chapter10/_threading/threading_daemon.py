"""
Потоки, являющеся и не являющиеся демонами.

До сих пор во всех примерах предполагалось, что выход из программы неявно
откладывался до тех пор, пока все потоки не завершат свою работу. Однако
иногда программы могут создавать потоки-демоны, выполнение которых не блокирует
выход из основной программы. Потоки такого типа удобно использовать
в службах в тех случаях, когда прерывание работы потока затруднено или же его
преждевременное завершение не может привести к потере или повреждению данных
(например, если поток генерирует контрольные сигналы в целях мониторинга службы).
Для указания того, что поток создается как демон, следует передать аргумент
daemon=True его конструктору или вызвать метод set_daemon (), передав ему
значение True. Создаваемые потоки по умолчанию не являются демонами.
"""
import threading
import time
import logging


def daemon():
    logging.debug('Starting')
    time.sleep(0.2)
    logging.debug('Existing')


def non_deamon():
    logging.debug('Starting')
    logging.debug('Existing')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s'
)

if __name__ == '__main__':
    d = threading.Thread(name='deamon', target=daemon, daemon=True)
    t = threading.Thread(name='non-daemon', target=non_deamon)
    d.start()
    t.start()
    # Чтобы дождаться завершения работы потока-демона, следует использовать метод join().
    # По умолчанию метод join() блокируется на бесконечное время, однако ему
    # можно передать аргумент в виде значения c плавающей точкой — тайм-аута, определяющего
    # предельное время ожидания перехода потока в неактивное состояние.
    # Если поток не успеет завершиться в течение указанного времегги, то метод
    # join() в любом случае выполнит возврат.
    d.join(0.1)
    print('d.isAlive()', d.is_alive())
    t.join()

