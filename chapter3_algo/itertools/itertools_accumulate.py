# accumulate() обрабатывает входные итерируемые объекты, передавая n-й и (n+1)-й элементы
# функции и возращаю получаемый с помощью этой функции результат вместо входных значений
# Функция по умл. суммирует два значения, поэтому функцию accumulate() можно исп. для получения
# накопительной суммы
from itertools import accumulate

print(list(accumulate(range(5))))
print(list(accumulate('abcde')))


def f(a, b):
    print(a, b)
    print('result - ', b + a + b)
    return b + a + b


print(list(accumulate('abcde', f)))
print(list(accumulate(range(5), f)))
