# Вместо вложенных циклов, выполняющих итерации по нескольким последо­
# вательностям, часто можно использовать функцию product (), возвращающую
# итерируемый объект, значениями которого являются декартовы произведения входных значений.
from itertools import *

FACE_CARDS = ('J', 'Q', 'K', 'A')
SUITS = ('H', 'D', 'C', 'S')
DECK = list(
    product(
        chain(range(2, 11), FACE_CARDS),
        SUITS,
    )
)

for card in DECK:
    print(card)

for card in DECK:
    print('{:>2}{}'.format(*card), end=' ')
    if card[1] == SUITS[-1]:
        print()


# Чтобы вычислить произведение последовательности на саму себя, слудует указать кол-во повторений
def show(iterable):
    for i, item in enumerate(iterable, 1):
        print(item, end=' ')
        if (i % 3) == 0:
            print()
    print()


print('Repeat 2:\n')
show(list(product(range(3), repeat=2)))

print('Repeat 3:\n')
show(list(product(range(3), repeat=3)))
