# 10.5.9.2 Эхо-клиент
import asyncio
import logging
import ssl
import sys


async def echo_client(address, messages):
    """
    Аналогичные изменения должны быть внесены также в клиентскую программу.
    В прежней версии для создания соединения сокета c сервером используется
    функция open_connection().
    Для создания безопасного сокета на стороне клиента следует вновь использовать
    экземпляр SSLContext. Поскольку аутентификация клиента не навязывается,
    необходимо загрузить только сертификат.
    """
    log = logging.getLogger('echo_client')
    log.debug('connection to {} port {}'.format(*address))
    ssl_context = ssl.create_default_context(
        ssl.Purpose.SERVER_AUTH,
    )
    ssl_context.check_hostname = False
    ssl_context.load_verify_locations('pymotw.crt')
    reader, writer = await asyncio.open_connection(*address, ssl=ssl_context)

    """
    В клиенте требуется внесение еще одного небольшого изменения. Поскольку
    SSL-соединение не поддерживает отправку метки конца файла (EOF), клиент 
    использует байт NULL в качестве завершающего символа сообщения. В прежней 
    версии цикла отправки сообщений для этой цели используется метод write_eof().
    Новая версия отправляет нулевой байт (b'Xx00') в качестве признака конца сообщения.
    """
    for msg in messages:
        writer.write(msg)
        log.debug('sending {!r}'.format(msg))
    writer.write(b'\x00')
    await writer.drain()

    log.debug('waiting for response')
    while True:
        data = await reader.read(128)
        if data:
            log.debug('received {!r}'.format(data))
        else:
            log.debug('closing')
            writer.close()
            return


if __name__ == '__main__':

    MESSAGES = [
        b'This is the message. ',
        b'It will be sent ',
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
    try:
        event_loop.run_until_complete(
            echo_client(SERVER_ADDRESS, MESSAGES)
        )
    finally:
        log.debug('closing event loop')
        event_loop.close()
