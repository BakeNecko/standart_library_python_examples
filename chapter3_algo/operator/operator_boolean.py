from operator import not_, truth, is_, is_not

a = -1
b = 5

print('a = ', a)
print('b = ', b)
print()

print('not_(a)      :', not_(a))  # not(a)
print('truth(a)     :', truth(a))  # bool(a)
print('is_(a,b)     :', is_(a, b))  # a is b
print('is_not(a,b)  :', is_not(a, b))  # a is not b
