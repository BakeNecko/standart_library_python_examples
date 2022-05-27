# 10.5.6.3 Обработка фоновых операций по мере их завершения
"""
Функция os_completed() - это генератор, который управляет выполнением
списка переданных ему программ и возвращает результаты по одному
за раз по мере завершения выполняющихся сопргграмм. Как и функция wait(),
функция os_completed() не гарантирует очередность завершения программ,
но ждать, пока завершатся все фоновые операции, прежде чем предпринимать
какие-либо другие действия, необязательно.
"""
import asyncio


async def phase(i):
    print(f'in phase {i}')
    await asyncio.sleep(0.5 - (0.1 * i))
    print(f'done with phase {i}')
    return f'phase {i} result'


async def main(num_phases):
    print('starting main')
    phases = [
        phase(i)
        for i in range(num_phases)
    ]
    print('waiting for phases to complete')
    results = []
    for next_to_complete in asyncio.as_completed(phases):
        answer = await next_to_complete
        print(f'received anser {answer}')
        results.append(answer)
    print(f'results: {results}')
    return results


if __name__ == '__main__':
    """
    Этот пример начинается c запуска нескольких фоновых фаз, которые завершаются 
    в порядке, обратном порядку их запуска. По исчерпании генератора цикл
    ожидает результаты работы сопрограммы, используя ключевое слово await.
    """
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main(5))
    finally:
        print('close event_loop')
        event_loop.close()
