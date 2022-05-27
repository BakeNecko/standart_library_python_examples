"""
В предыдущем примере (multiprocessing_semaphore) список активных процессов
поддерживался централизованно  в экземпляре ActivePool объектом списка
специального типа, предоставляемым классом Manager. Этот класс отвечает
за координацию информациио разделяемом состоянии между всеми своими
пользователями.
"""
import multiprocessing


def worker(d, key, value):
    d[key] = value


if __name__ == '__main__':
    """
    Поскольку этот список создается посредством менеджера, он разделяется всеми 
    процессами, а его обновления видимы в каждом из них. Поддерживаются также словари.
    """
    mgr = multiprocessing.Manager()
    d = mgr.dict()
    jobs = [
        multiprocessing.Process(
            target=worker,
            args=(d, i, i * 2)
        )
        for i in range(10)
    ]
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    print('Result:', d)
