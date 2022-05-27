# 10.5.6.2 Сбор результатов от сопрограмм
"""
Если фоновые фазы определены корректно и имеют значение лишь их результаты,
то для ожидания завершения нескольких операций целесообразно использовать
функцию gather().
"""
import asyncio


async def phase1():
    print('in phase 1')
    await asyncio.sleep(2)
    print('done with phase1')
    return 'phase result'


async def phase2():
    print('in phase 2')
    await asyncio.sleep(1)
    print('done with phase2')
    return 'phase2 result'


async def main():
    print('starting main')
    print('waiting for phases to complete')
    results = await asyncio.gather(
        phase1(),
        phase2(),
    )
    print('results: {!r}'.format(results))


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main())
    finally:
        print('close event_loop')
        event_loop.close()
