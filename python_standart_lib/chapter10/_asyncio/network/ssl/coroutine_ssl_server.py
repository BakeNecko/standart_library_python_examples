import asyncio
import logging
import ssl
import sys


async def echo(reader: 'asyncio.StreamReader', writer: 'asyncio.StreamWriter'):
    address = writer.get_extra_info('peername')
    _log = logging.getLogger('echo_{}_{}'.format(*address))
    _log.debug('connection accepted')

    while True:
        data = await reader.read(128)
        terminate = data.endswith(b'\x00')
        data = data.rstrip(b'\x00')
        if data:
            _log.debug('received {!r}'.format(data))
            writer.write(data)
            await writer.drain()
            _log.debug('sent {!r}'.format(data))
        if not data or terminate:
            log.debug('message terminated, closing connection')
            writer.close()
            return


if __name__ == '__main__':
    SERVER_ADDRESS = ('localhost', 10000)
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(name)s: %(message)s',
        stream=sys.stderr,
    )
    log = logging.getLogger('main')

    event_loop = asyncio.get_event_loop()
    # Сертификат создается с использованием имени хоста pymotw.com.
    # При выполнении примера на другом хосте это имя не будет
    # корректным, поэтому следует отменить его проверку
    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_context.check_hostname = False
    ssl_context.load_cert_chain('pymotw.crt', 'pymotw.key')

    # Создать сервер и позволить ему завершить сопрограмму до
    # запуска реального цикла событий
    factory = asyncio.start_server(echo, *SERVER_ADDRESS, ssl=ssl_context)

    server = event_loop.run_until_complete(factory)
    log.debug('starting up on {} port {}'.format(*SERVER_ADDRESS))
    try:
        event_loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        log.debug('closing server')
        server.close()
        event_loop.run_until_complete(server.wait_closed())
        log.debug('closing event loop')
        event_loop.close()
