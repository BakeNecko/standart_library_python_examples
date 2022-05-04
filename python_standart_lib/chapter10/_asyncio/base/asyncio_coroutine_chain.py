# 10.5.2.3 Цепочка сопрограмм
"""
Одна сопрограмма может запустить другую и ожидать её результатов, что
упрощает разбиение задачи на повторно используемые части.
Следующий пример имеет 2 фазы, которые должны быть выполнены по очерди,
номогут выполняться параллельно с другими операциями.
"""
import asyncio


async def outer():
    print('in outer')
    print('waiting for result1')
    result1 = await phase1()
    print('waiting for result2')
    result2 = await phase2(result1)
    return result1, result2


async def phase1():
    print('in phase1')
    return 'result1'


async def phase2(arg):
    print('in pahse2')
    return f'result2 derived from {arg}'

if __name__ == '__main__':
    """
    Вместо добавления в цикл новых сопрограмм можно использовать ключевое
    слово await. Поскольку поток выполнения уже находится в теле сопрограммы,
    управляемой циклом, нет нужды сообщать циклу о необходимости управления 
    новыми сопрограммами.
    """
    event_loop = asyncio.get_event_loop()
    try:
        return_value = event_loop.run_until_complete(outer())
        print('return value: {!r}'.format(return_value))
    finally:
        event_loop.close()
