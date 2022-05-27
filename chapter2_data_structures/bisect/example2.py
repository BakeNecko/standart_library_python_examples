"""
insort_right() - вставляет элемент после сущ. значения
insort_left() - вставляет эл. перед сущ. значением
"""
import bisect

values = [14, 85, 77, 26, 50, 45, 66, 79, 10, 3, 84, 77, 1]

print('New Pos Contents')
print('--- --- --------')

if __name__ == '__main__':
    l = []
    for i in values:
        position = bisect.bisect_left(l, i)
        bisect.insort_left(l, i)
        print('{:3} {:3}'.format(i, position), l)
