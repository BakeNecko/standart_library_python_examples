from itertools import zip_longest

for i in zip([1, 2, 3], ['a', 'b', 'c']):
    print(i)

# Чтобы продолжить работу даже когда один из списов кончается исп. zip_longest
r1 = range(3)
r2 = range(2)

print('zip stops early:')
print(list(zip(r1, r2)))

r1 = range(3)
r2 = range(2)

print('\nzip_longest processes all of the values:')
print(list(zip_longest(r1, r2)))

print('\nzip_longest processes all of the values with default:')
print(list(zip_longest(r1, r2, fillvalue='Default')))
