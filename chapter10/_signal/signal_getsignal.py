"""
10.2.2 Получние информации о зар. обработчиках сигналов

Чтобы увидеть, какие обработчики зарегистрированны для сигнала, используйте
функцию getsignal(). В качестве аргумента ей передается номер сигнала.
Возвращаемым значением является зарег. обработчик ли одно из
спец. заначений SIG_IGN (если данный сиг. игнорируется),
SIG_DFL (если исп. поведение, заданное по умл)
или None (если сущ. обаботчик сигналов зарег. в С, а не из Python)
"""
import signal


def alarm_received(n, stack):
    return


signal.signal(signal.SIGALRM, alarm_received)

signals_to_names = {
    getattr(signal, n): n
    for n in dir(signal)
    if n.startswith('SIG') and '_' not in n
}

if __name__ == '__main__':
    for s, name in sorted(signals_to_names.items()):
        handler = signal.getsignal(s)
        if handler is signal.SIG_DFL:
            handler = 'SIG_DFL'
        elif handler is signal.SIG_IGN:
            handler = 'SIG_IGN'
        print('{:<10} ({:2d})'.format(name, s), handler)
