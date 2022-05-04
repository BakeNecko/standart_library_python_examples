"""
Экземпляр Future также можно использовать вместе c ключевым словом
await, как показано в следующем примере.
"""
import asyncio


def mark_done(future, result):
    print('settting future result to {!r}'.format(result))
    future.set_result(result)


async def main(loop: 'asyncio.AbstractEventLoop'):
    all_done = asyncio.Future()

    print('scheduling mark_done')
    loop.call_soon(mark_done, all_done, 'the result')

    result = await all_done
    print('returned result: {!r}'.format(result))


if __name__ == '__main__':
    """
    Результат, хранящийся в экземпляре Future, возвращается c помощью 
    ключевого слова await, поэтому во многих случаях один и тот же код 
    может работать как c обычной сопрограммой, так и c экземпляром Future.
    """
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main(event_loop))
    except:
        event_loop.close()
