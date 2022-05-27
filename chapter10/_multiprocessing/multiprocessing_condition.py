# 10.4.13 Синхронизация операций
"""
Класс Condition, предаставляющий условие позволяет синхронизировать отдельные
ветаи вычислений так, чтобы один из них выполнялись параллельно, тогда как другие
последовательно, даже если они принадлежат отдельным процессам.
"""
import multiprocessing
import time


def stage_1(cond: 'multiprocessing.Condition'):
    """Выполнять первый этап работы, а затем увдомить stage_2 для продолжения"""
    name = multiprocessing.current_process().name
    print('Starting', name)
    with cond:
        print(f'{name} done and ready for stage_2')
        cond.notify_all()


def stage_2(cond: 'multiprocessing.Condition'):
    """Дождаться условия, сообщающего, что stage_1 завершен"""
    name = multiprocessing.current_process().name
    print('Starting', name)
    with cond:
        cond.wait()
        print(f'{name} running (stage_2)')


if __name__ == '__main__':
    """
    В этом примере второй этап вычислений выполняется параллельно обоими
    процессами, но только после того, как выполнен первый этап.
    """
    condition = multiprocessing.Condition()
    s1 = multiprocessing.Process(
        name='s1',
        target=stage_1,
        args=(condition,)
    )
    s2_clients = [
        multiprocessing.Process(
            name=f'stage_2[{i}]',
            target=stage_2,
            args=(condition,),
        )
        for i in range(1, 3)
    ]
    for c in s2_clients:
        c.start()
        time.sleep(1)
    s1.start()

    s1.join()
    for c in s2_clients:
        c.join()
