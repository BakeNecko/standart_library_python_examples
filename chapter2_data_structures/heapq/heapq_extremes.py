"""
2.4.4 Получение наибольших и наименьших элементов кучи
"""
import heapq
from heapq_heapdata import data

if __name__ == '__main__':
    """
    nlargest()/nsmallest() наиболее эфф. лишь при относительно
    небольших значениях n > 1.
    """
    print('all          :', data)
    print('3 largest    :', heapq.nlargest(3, data))
    print('from sort    :', list(reversed(sorted(data)[-3:])))
    print('3 smallest   :', heapq.nsmallest(3, data))
