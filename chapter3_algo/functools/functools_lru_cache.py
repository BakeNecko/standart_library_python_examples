# LRU - (eng: least recently used - вытесняется элемент, не использованный дольше всех)
# Аргументы функции исп. для создания хэш-значения, которое сопостовляется с результатом.
# Послед. вывозы функции с теми же аргументами будут заменяться извлечением соответ. значения из кеша
# Также этот декор. добавляет методы, обеспечивающие проверку сост. (cache_info()) и очистку (cache_clear()) кеша

# Ключи для кеша, упарвляемого фу-ей lru_cache() должны быть хешируемы
# поэтому нельзя передать в аргументы функции например список/list
import functools


@functools.lru_cache()  # maxsize это размер кэша
def expensive(a, b):
    print(f'expensive: ({a},{b})')
    return a * b


MAX = 2

print('First set of calls:')
for i in range(MAX):
    for j in range(MAX):
        expensive(i, j)
print(expensive.cache_info())

print('\nSecond set of calls:')
for i in range(MAX + 1):
    for j in range(MAX + 1):
        expensive(i, j)
print(expensive.cache_info())

print('\nClearing cache:')
expensive.cache_clear()
print(expensive.cache_info())

print('\nThird set of calls:')
for i in range(MAX):
    for j in range(MAX):
        expensive(i, j)
print(expensive.cache_info())
