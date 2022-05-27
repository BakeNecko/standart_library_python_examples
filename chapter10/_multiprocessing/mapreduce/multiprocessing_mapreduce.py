# 10.4.18 Реализация MapReduce
"""
В системе, основанной на библиотеке MapReduce, входные данные подвергаются
предварительной обработке, в ходе которой они разделяются на порции, обрабатываемые
отдельными экземплярами рабочих объектов. Каждая такая порция входных данных
отображается (map) на промежуточное состояние c использованием простого преобразования.
Затем промежуточные данные группируются на основе ключей таким образом,
чтобы все родственные значения хранились вместе. Наконец, выполняется
свертка (reduce) сгруппированных данных в результирующий набор.
"""
import collections
import itertools
import multiprocessing


class SimpleMapReduce:
    def __init__(self, map_func, reduce_func, num_workers=None):
        """
        :param map_func: Функция для отображения входных данных на промежуточные.
        Получчает 1н аргумент в качестве входого значения и возвращает кортеж
        с ключом и значением для свертки.
        :param reduce_func: Функция для свертки сгруппированной версии промежуточных
        данных в финальный вывод. В качестве аргумента получает ключ, созданный map_func,
        и последовательность значений, связанных с этим клюсом.
        :param num_workers: Число содаваемых рабочих процессов в пуле. По умл. Равно
        число процессоров текущего хоста.
        """
        self.map_func = map_func
        self.reduce_func = reduce_func
        self.pool = multiprocessing.Pool(num_workers)

    @staticmethod
    def partition(mapped_values):
        """Организует отображаемые значения по ключам.
        Возвращает неотсорт. послед. кортежей
        с ключом и послед. значений"""
        partitioned_data = collections.defaultdict(list)
        for key, value in mapped_values:
            partitioned_data[key].append(value)
        return partitioned_data.items()

    def __call__(self, inputs, chunksize=1):
        """
        Обработать входные значения через предоствленные функции отображения и свертки
        :param inputs:  Интерируемый объект, содержащий входные данные для обработки
        :param chunksize: Фрагмент входных данных для передачи каждому рабочему процессу.
        Это можно использовать для настройки производительности во время фазы отображения.
        """
        map_response = self.pool.map(
            self.map_func,
            inputs,
            chunksize=chunksize
        )
        partitioned_data = self.partition(
            itertools.chain(*map_response)
        )
        reduced_values = self.pool.map(
            self.reduce_func,
            partitioned_data,
        )
        return reduced_values
