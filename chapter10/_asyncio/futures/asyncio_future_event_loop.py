# 10.5.4.1 Ожидание завершения задания экземпляром Future
"""
Экземпляр Future (фьючерс) действует подобно сопрограмме, поэтомулюбые
приемы, используемые для ожидания завершения сопрограммы, также применимы
к фьючерсам. В следующем примере объект фьючерса передается методу
run_until_complete() цикла.
"""
import asyncio


def mark_done(future: 'asyncio.Future', result):
    print('setting future result ro {!r}'.format(result))
    future.set_result(result) # future (state) = done



if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    try:
        all_done = asyncio.Future()
        print('scheduling mark_done')
        event_loop.call_soon(mark_done, all_done, 'the result')
        print('entering event loop')
        result = event_loop.run_until_complete(all_done)
        print('returned result: {!r}'.format(result))
    finally:
        print('closing event loop')
        event_loop.close()
