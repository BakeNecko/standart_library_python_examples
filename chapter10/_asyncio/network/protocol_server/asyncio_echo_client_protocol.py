# 10.5.8.2 Эхо-клиент
"""
Создание клиента с использованием класса протокола очень похоже на
создание сервера. Код клиента также начинается c импорта модулей asyncio и
logging (раздел 14.80) с последующим созданием объекта цикла событий.
"""
import asyncio
import functools
import logging
import sys


class EchoClient(asyncio.Protocol):
    """
    Клиентский класс протокола определяет те же методы, что и серверный, но
    с другой реализацией. Конструктор класса получает два аргумента: список
    сообщений, подлежащих отправке, и экземпляр Future, используемый для
    отправки сигнала, означающего, что клиент завершил рабочий цикл,
    получив ответ от сервера.
    """

    def __init__(self, messages, future):
        super(EchoClient, self).__init__()
        self.messages = messages
        self.log = logging.getLogger('EchoClient')
        self.f = future

    def connection_made(self, transport: 'asyncio.Transport') -> None:
        """
        После успешного соединения с сервером клиент немедленно приступает к
        обмену данными. Сообщения отправляются по одному за раз, хотя базовый сетевой
        код может объединить несколько сообщений в одной пересылке. Когда вся
        последовательность сообщений исчерпывается, посылается метка конца файла EOE
        Несмотря на то, что создается впечатление, будто все данные отправляются немедленно,
        в действительности объект transport буферизует исходящие данные и устанавливает
        функцию обратного вызова, которая осуществляет фактическую передачу данных,
        когда буфер сокета готов их принять. Эта обработка выполняется прозрачным образом,
        поэтому код приложения может быть написан так,
        словно операции ввода-вывода выполняются немедленно.
        """
        self.transport = transport
        self.address = transport.get_extra_info('peername')
        self.log.debug(
            'connection to {} port {}'.format(*self.address)
        )
        # Здесь можно было бы использовать метод
        # transport.writelines(), но это затруднило бы
        # представление каждой части отправляемого сообщения
        for msg in self.messages:
            transport.write(msg)
            self.log.debug('sending {!r}'.format(msg))
        if transport.can_write_eof():
            transport.write_eof()

    def data_received(self, data: bytes) -> None:
        self.log.debug('received {!r}'.format(data))

    def eof_received(self) -> None:
        """
        Наконец, если получена метка конца файла или соединение закрыто на стороне
        сервера, локальный объект transport закрывается, а объект фьючерса
        помечается как завершивший работу вызовом метода set_result().
        """
        self.log.debug('received EOF')
        self.transport.close()
        if not self.f.done():
            self.f.set_result(True)

    def connection_lost(self, exc):
        self.log.debug('server closed connection')
        self.transport.close()
        if not self.f.done():
            self.f.set_result(True)
        super(EchoClient, self).connection_lost(exc)


if __name__ == '__main__':
    MESSAGES = [
        b'This is the message.',
        b'IT will be sent ',
        b'in parts.'
    ]
    SERVER_ADDRESS = ('localhost', 10000)

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(name)s: %(message)s',
        stream=sys.stderr,
    )
    log = logging.getLogger('main')
    event_loop = asyncio.get_event_loop()
    """
    Обычно соединение создается путем передачи класса протокола циклу событий. 
    В данном случае, поскольку цикл событий не имеет возможности передать дополнительные 
    аргументы конструктору протокола, необходимо обернуть класс клиента c помощью функции 
    partial(), передав ей в качестве аргументов список сообщений и экземпляр Future. 
    Далее этот новый вызываемый объект может быть использован вместо класса при вызове 
    метода create_connection() для подключения клиента.
    """
    client_completed = asyncio.Future()

    client_factory = functools.partial(
        EchoClient,
        messages=MESSAGES,
        future=client_completed,
    )
    factory_coroutine = event_loop.create_connection(
        client_factory,
        *SERVER_ADDRESS
    )
    """
    Чтобы инициировать выполнение клиента, цикл событий запускается один
    раз c сопрограммой для создания клиента, а второй — c экземпляром Future, 
    передаваемым клиенту для обмена данными после завершения работы. 
    Использование двух вызовов позволяет избежать создания бесконечного цикла в 
    клиентской программе, которая, вероятно, захочет завершить выполнение после обмена
    данными c сервером. Если бы использовался только первый вызов, ожидающий
    создания клиента сопрограммой, то не исключено, что он не смог бы обработать
    все данные ответа и закрыть соединение c сервером надлежащим образом.
    """
    log.debug('waiting for client to complete')
    try:
        event_loop.run_until_complete(factory_coroutine)
        # Нужно, чтобы 100% закрыть соедниеие с сервером
        event_loop.run_until_complete(client_completed)
    finally:
        log.debug('closing event loop')
        event_loop.close()
