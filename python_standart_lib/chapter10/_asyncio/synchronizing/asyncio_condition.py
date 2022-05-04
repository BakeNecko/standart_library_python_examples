# 10.5.7.3 Условия
"""
Класс Condition работает аналогично классу Event, за исключением того, что
вместо уведомления всех ожидающих сопрограмм можно ограничить количество
тех из них, которые будут пробуждаться, передав соответствующий аргумент
методу notify()
"""
import asyncio


async def consumer(condition: 'asyncio.Condition', n: int):
    async with condition:
        print(f'consumer {n} is waiting')
        await condition.wait()
        print(f'consumer {n} triggered')
    print(f'ending consumer {n}')


async def manipulate_condition(condition: 'asyncio.Condition'):
    print('starting manipulate_condition')

    # Пауза, позволяющая потребителям запуститься
    await asyncio.sleep(0.1)

    for i in range(1, 3):
        async with condition:
            print(f'notify {i} consumers')
            condition.notify(n=i)
        await asyncio.sleep(0.1)

    async with condition:
        print('notify remaining consumers')
        condition.notify_all()
    print('ending manipulate_condition')


async def main(loop: 'asyncio.AbstractEventLoop'):
    # создать условие
    condition = asyncio.Condition()

    # Создать список задач, следящих за условием
    consumers = [
        consumer(condition, i)
        for i in range(5)
    ]

    # Запланировать задачу для манипулирования
    # переменной condition
    loop.create_task(manipulate_condition(condition))

    # Ждать завершения потребителей
    await asyncio.wait(consumers)


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main(event_loop  ))
    finally:
        print('close event_loop')
        event_loop.close()
