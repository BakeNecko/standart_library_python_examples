#  10.5.11.1 Получение IP-адреса по имени хоста
"""
Сопрограмма getaddrinfo () преобразует имя хоста и номер порта в IP- или
1Ру6-адрес. Как и в случае версии этой функции, содержащейся в модуле socket
(раздел 11.2), возвращаемое значение представляет собой список кортежей,
содержащих следующие пять элементов информации
    - семейство адресов;
    - тип адреса;
    - протокол;
    - каноническое имя сервера;
    - кортеж адреса сокета, пригодный для открытия соединения с сервером
    через первоначально указанный порт.
Запросы могут фильтроваться протоколом. В следующем примере фильтр
гарантирует, что возвращаться будут только отвеы, использующие протокол TCP.
"""
import asyncio
import socket

TARGETS = [
    ('pymotw.com', 'https'),
    ('doughellmann.com', 'https'),
    ('python.org', 'https'),
]


async def main(loop: 'asyncio.AbstractEventLoop', targets: 'TARGETS'):
    for target in targets:
        info = await loop.getaddrinfo(
            *target,
            proto=socket.IPPROTO_TCP,
        )
        for host in info:
            print('{:20}: {}'.format(target[0], host[4][0]))


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main(event_loop, TARGETS))
    finally:
        event_loop.close()
