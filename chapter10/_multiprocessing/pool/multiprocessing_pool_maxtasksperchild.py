"""
По умолчанию экземпляр Pool создает фиксированное количество рабочих
процессов и передает им задачи до тех пор, пока все они не будут исчерпаны.
C помощью параметра maxtasksperchild можно указать максимальное количество
задач, передаваемых одному процессу, после чего он будет перезапущен, что
позволяет предотвратить завладение чрезмерно большим количеством ресурсов
длительно выполняющимися процессами.
"""
import multiprocessing


def do_calculation(data):
    return data * 2


def start_process():
    print('Starting', multiprocessing.current_process().name)


if __name__ == '__main__':
    """
    Пул перезапускает рабочие процессы после выполнения ими отведенного 
    количества задач, даже если все задачи уже исчерпаны. Как следует из 
    приведенного ниже вывода, в данном примере создаются (multiprocessing.cpu_count() * 2)
    процессов, хотя имеется только 10 задач и каждый рабочий процесс 
    способен выполнить две задачи за один раз.
    """
    inputs = list(range(10))
    print('Input   :', inputs)

    builtin_outputs = map(do_calculation, inputs)
    print('Built-in:', list(builtin_outputs))

    pool_size = multiprocessing.cpu_count() * 2
    pool = multiprocessing.Pool(
        processes=pool_size,
        initializer=start_process,
        maxtasksperchild=2,
    )
    pool_outputs = pool.map(do_calculation, inputs)
    pool.close()  # Больше нет задач
    pool.join()  # Обернуть текущие задачи

    print('Pool   :', pool_outputs)
