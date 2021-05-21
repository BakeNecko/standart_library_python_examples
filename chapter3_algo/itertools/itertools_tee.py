from itertools import islice, count, tee

r = islice(count(), 5)
i1, i2 = tee(r)

print('i1:', list(i1))
print('i2:', list(i2))

# !!! После создания итераторов с помощью tee исходный итератор не должен использоваться
# Иначе использованные значения будут утерянны
r = islice(count(), 5)
i1, i2 = tee(r)

print('r:', end=' ')
for i in r:
    print(i, end=' ')
    if i > 1:
        break
print()
print('i1: ', list(i1))
print('i2: ', list(i2))
