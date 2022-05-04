# 10.5.2.2 Возврат значений из сопрограмм
"""
Значение, возвращаемое сопрограммой, передается коду, который её запустил
и ожидает её завершения
"""
import asyncio


async def coroutine():
    print('in coroutine')
    return 'result'

if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    try:
        return_value = event_loop.run_until_complete(
            coroutine()
        )
        print('it returned: {!r}'.format(return_value))
    finally:
        event_loop.close()
