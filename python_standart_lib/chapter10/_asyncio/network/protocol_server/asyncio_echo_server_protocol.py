# 10.5.8.1 Эхо-сервер
"""
Код эхо-сервера начинается с импорта модулей asyncio и logging (раздел 14.80)
и создания объекта цикла событий.
"""
import asyncio
import typing
import logging
import sys


class EchoServer(asyncio.Protocol):
    """
    Далее определяется подкласс asyncio.Protocol, обеспечивающий взаимодействие
    c клиентом. Методы объекта протокола вызываются в ответ па события,
    связанные с сокетом сервера.
    """

    def connection_made(self, transport: 'asyncio.Transport'):
        """
        Подключение каждого нового клиента инициирует вызов метода connection_
        made(). Аргумент transport — это экземпляр asyncio.Transport,
        предоставляющий абстракцию для выполнения асинхронных операций ввода-вывода с
        использованием сокета. Различные типы протоколов связи предоставляют различные
        реализации объекта transport c одним и тем же API. Например, для работы с
        сокетами и для работы с каналами подпроцессов используются отдельные
        транспортные классы. Адрес клиента доступен из объекта transport через метод
        get_extra_info(), специфический для каждой реализации.
        """
        self.transport = transport
        self.address = transport.get_extra_info('peername')
        self.log = logging.getLogger(
            'EchoServer_{}_{}'.format(*self.address)
        )

    def data_received(self, data):
        """
        После установления соединения, когда клиент отправил данные серверу,
        вызывается метод data_received() протокола, который передает поступившие
        данные для их обработки. Данные передаются в виде байтовой строки, за
        декодирование и надлежащую обработку которой отвечает приложение. В следующем
        фрагменте кода результаты протоколируются, а ответ немедленно отправляется
        обратно клиенту посредством вызова метода transport.write()
        """
        self.log.debug('received {!r}'.format(data))
        self.transport.write(data)
        self.log.debug('sent {!r}'.format(data))

    def eof_received(self):
        """
        Некоторые объекты transport поддерживают специальные метки конца
        файла (EOF). Когда встречается метка EOF, вызывается метод eof_received().
        В этой реализации метка EOF отправляется обратно клиенту в качестве
        подтверждения того, что она была получена. Поскольку не все объекты transport
        поддерживают метку EOF, данный протокол запрашивает у объекта transport,
        безопасно ли ее отправлять.
        """
        self.log.debug('received EOF')
        if self.transport.can_write_eof():
            self.transport.write_eof()

    def connection_lost(self, exc: typing.Union[Exception, None]) -> None:
        """
        Когда соединение закрывается, будь то обычным способом или в результате
        возникновения ошибки, вызывается метод connection_lost (). В случае
        возникновения ошибки аргумент error содержит объект исключения,
        в противном случае он содержит значение None.
        """
        if exc:
            self.log.debug(f'Error: {exc}')
        self.transport.close()


if __name__ == '__main__':
    """
    Запуск сервера осуществляется в два этапа. Во-первых, приложение сообщает
    циклу событий о том, что необходимо создать новый объект сервера, используя
    заданные класс протокола, имя хоста и сокет. Метод create_server() — это сопрограмма, 
    поэтому для фактического запуска сервера результаты должны быть обработаны циклом событий. 
    По завершении работы сопрограммы создается экземпляр asyncio.Server, связанный c циклом событий
    """
    SERVER_ADDRESS = ('localhost', 10000)

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(name)s: %(message)s',
        stream=sys.stderr,
    )
    log = logging.getLogger('main')
    event_loop = asyncio.get_event_loop()
    # Создать сервер и позволить циклу завершить сопрограмму, прежде
    # чем запустить реальный цикл событий
    factory = event_loop.create_server(EchoServer, *SERVER_ADDRESS)  # return coroutine
    server = event_loop.run_until_complete(factory)
    log.debug('startin up on {} port {}'.format(*SERVER_ADDRESS))
    """
    На следующем этапе должен быть запущен цикл событий, который будет обрабатывать 
    события и клиентские запросы. Для длительно выполняющихся служб это проще всего обеспечить, 
    вызвав метод run_forever(). В случае прекращения выполнения цикла событий из кода приложения 
    или посредством посылки сигнала процессу сервер можно закрыть для освобождения неиспользуемых сокетом
    ресурсов. После этого можно закрыть цикл событий, чтобы завершить обработку других сопрограмм 
    перед выходом из программы.
    """
    # Войти в бесконечный цикл событий для обработки всех соединений
    try:
        event_loop.run_forever()
    finally:
        log.debug('closing server')
        server.close()
        event_loop.run_until_complete(server.wait_closed())
        log.debug('closing event loop')
        event_loop.close()
