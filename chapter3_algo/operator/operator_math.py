from operator import abs, neg, pos, add, floordiv, mod, mul, pow, sub, and_, truediv, invert, lshift, or_, rshift, xor

a = -1
b = 5.0
c = 2
d = 6

print('a = ', a)
print('b = ', b)
print('c = ', c)
print('d = ', d)

print('\nPositive/Negative:')
print(f'abs({a}):', abs(a))
print(f'neg({a}):', neg(a))
print(f'neg({b}):', neg(b))
print(f'pos({a}):', pos(a))
print(f'pos({b}):', pos(b))

print('\nArithmetic:')
print(f'add({a}, {b}):', add(a, b))
print(f'floordiv({a}, {b}):', floordiv(a, b))
print(f'mod({a},{b}): ', mod(a, b))
print(f'mul({a},{b}): ', mul(a, b))
print(f'pow({c},{d}):', pow(c, d))
print(f'sub({b},{a}):', sub(b, a))
print(f'truediv({a},{b}):', truediv(a, b))
print(f'truediv({d},{c}):', truediv(d, c))

print('\nBitwise:')
print(f'and_({c}, {d}) :', and_(c, d))
print(f'invert({c}) :', invert(c))
print(f'lshift({c}, {d}) :', lshift(c, d))
print(f'or_({c}, {d}) :', or_(c, d))
print(f'rshift({d}, {c}) :', rshift(d, c))
print(f'xor({c}, {d}) :', xor(c, d))

