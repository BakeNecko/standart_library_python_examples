# Операторы для работы c последовательностями
from operator import *

a = [1, 2, 3]
b = ['a', 'b', 'c']

print('a = ', a)
print('b = ', b)

print('\nConstructive:')
print(f'concat({a}, {b}', concat(a, b))

print('\nSearching:')
print(f'containse({a}, 1)                     :', contains(a, 1))
print(f'containse({b}, "d")                   :', contains(b, "d"))
print(f'countOf({a}, 1)                       :', countOf(a, 1))
print(f'countOf({b}, "d")                     :', countOf(b, "d"))
print(f'indexOf({a}, 5)                       :', indexOf(a, 1))

print('\nAccess Items:')
print(f'getitem({b}, 1)                       :', getitem(b, 1))
print(f'getitem({b}, slice(1,3))              :', getitem(b, slice(1, 3)))
print(f'setitem({b}, 1, "d")                  :', end=' ')
setitem(b, 1, "d")
print(b)
print(f'setitem({a}, slice(1,3), [4,5]):', end=' ')
setitem(a, slice(1, 3), [4, 5])
print(a)

print('\nDestructive                   :')
print(f'delitem({b},1)                 :', end=' ')
delitem(b, 1)
print(b)
print(f'delitem({a}, slice(1,3))       :', end=' ')
delitem(a, slice(1, 3))
print(a)
