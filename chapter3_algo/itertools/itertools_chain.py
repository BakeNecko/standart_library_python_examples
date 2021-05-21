from itertools import chain

for i in chain([1, 2, 3], ['a'], ['b', 'c']):
    print(i, end=' ')
print()

# В тех случаях, когда объединяемы итерируемы оюъекты неизвестны заранее или должно опред. в режиме отлож-ых вычислений
# Для конструирования цепочки итераторов можно исп. функцию chain.from_iterable()


def make_iterables_to_chain():
    yield [1, 2, 3]
    yield ['a', 'b', 'c']


for i in chain.from_iterable(make_iterables_to_chain()):
    print(i, end=' ')
