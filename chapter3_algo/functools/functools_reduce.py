# reduce() получает вызываемый объект и последовательность данных в качестве аргументов
# Результатом её работы явл. единственное значение, основанное на вызове объекта со значениями последовательности
# И накоплении результатов
import functools


def do_reduce(a, b):
    print(f'do_reduce({a}, {b})')
    return a + b


data = range(1, 5, 99)  # 99 это начальное значение
print(data)
result = functools.reduce(do_reduce, data)
print(f'result: {result}')

print(f'Single item in sequence: {functools.reduce(do_reduce, [1])}')
print(f'Single item in sequence with initializer: {functools.reduce(do_reduce, [1], 99)}')
print(f'Empty sequence with initializer: {functools.reduce(do_reduce, [], 99)}')
try:
    print(f'Empty sequence: {functools.reduce(do_reduce, [])}')
except TypeError as err:
    print(f'ERROR: {err}')


class Primes:
    @staticmethod
    def stream():
        numbers = [x for x in range(3, 10001, 2)]  # only odd numbers
        for i in numbers:
            numbers = list(filter(lambda x: x % i == 0, numbers))
        return (i for i in [2] + numbers)


if __name__ == '__main__':
    p = Primes().stream()
    next(p)
    next(p)
    next(p)
