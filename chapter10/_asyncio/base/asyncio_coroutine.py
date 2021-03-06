# 10.5.2.1 Запус сопрограммы
"""
Цикл событий модуля asyncio может запустить сопрограмму различными
способами. Самый простой подход заключается в использовании метода
run_unil_complete() с непосредственной передачей ему объекта программы.
"""
import asyncio


async def coroutine():
    print('in coroutine')


if __name__ == '__main__':
    """
    Прежде всего необходимо получить ссылку на цикл событий. Для этого можно
    либо воспользоваться циклом, предлагаемым по умолчанию, либо создать 
    специфический экземпляр цикла. В данном примере используется цикл, заданный по
    умолчанию. Метод run_until__complete () запускает цикл c объектом сопрограммы 
    и завершает его, когда сопрограмма возвращает управление.
    """
    event_loop = asyncio.get_event_loop()
    try:
        coro = coroutine()
        print('entering event loop')
        event_loop.run_until_complete(coro)
    finally:
        print('closing event loop')
        event_loop.close()
