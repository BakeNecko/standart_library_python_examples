# 10.5.11.2 Получение имени хоста по IP-адресу
"""
Сопрограмма getnameinfo() работает в обратном направлении, преобразуя
IP-адрес в имя хоста, а номер порта - в имя протокола, если это возможно.
"""
import asyncio

TARGETS = [
    ('185.199.111.153', 443),
    ('185.199.109.153', 443),
    ('2606:50c0:8001::153', 443),
    ('138.197.63.241', 443),
]


async def main(loop: 'asyncio.AbstractEventLoop', targets: 'TARGETS'):
    for target in targets:
        info = await loop.getnameinfo(target)
        print('{:15}: {} {}'.format(target[0], *info))


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main(event_loop, TARGETS))
    finally:
        event_loop.close()
