# 10.5.7.4 Очереди
"""
Класс asyncio.Queue предоставляет для сопрограмм структуру данных,
организованную по принципу “первым пришел — первым ушел”, которая работает во
многом подобно структурам, предоставляемым классами aqueue.Queue для потоков
и multiprocessing. Queue для процессов.
"""
import asyncio


async def consumer(n, q: 'asyncio.Queue'):
    print(f'consumer {n}: starting')
    while True:
        print(f'consumer {n}: waitin for item')
        item = await q.get()
        print(f'consumer {n}: has item {item}')
        if item is None:
            # None - сигнал стоп "таблетка"
            q.task_done()
            break
        else:
            await asyncio.sleep(0.01 * item)
            q.task_done()
    print(f'consumer {n}: ending')


async def producer(q: 'asyncio.Queue', num_workers: int):
    print('producer: starting')
    # Добавить некоторое количество задач в очередь
    # для имитации выполнения работы
    for i in range(num_workers * 3):
        await q.put(i)
        print(f'producer: added task {i} to the queue')
    # Доавбить в очередь значениея None в качестве сигналов,
    # предписывающих потребителям прекратить выполнение
    print('producer: adding stop singals to the queue')
    for i in range(num_workers):
        await q.put(None)
    print('producer: waiting for queue to empty')
    await q.join()
    print('producer: ending')


async def main(loop: 'asyncio.AbstractEventLoop', num_consumers):
    # Создать очередь фиксированного размера, чтобы производитель
    # блокировался до тех пор, пока потребители не извлекут
    # некоторое кол-во элементов
    q = asyncio.Queue(maxsize=num_consumers)

    # Запланировать задачи потребителей
    consumers = [
        loop.create_task(consumer(i, q))
        for i in range(num_consumers)
    ]

    # Запланировать задачи производителей
    prod = loop.create_task(producer(q, num_consumers))
    # Ждать завершения работы всех сопрограмм
    await asyncio.wait(consumers + [prod])


if __name__ == '__main__':
    """
    Операции добавления элементов c помощью метода put() и удаления c помощью 
    метода get() выполняются как асинхронные, поскольку либо размер очереди 
    может быть фиксированным (блокируется добавление в нее новых элементов), 
    либо очередь может быть пустой (блокируется извлечение элемента).
    """
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main(event_loop, 2))
    finally:
        print('close event_loop')
        event_loop.close()
