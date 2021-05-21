# Функция compress() предлогает способ фильтрации содержимого итерируемого объекта.
# Вместо того, чтобы вызывать функцию, она исп. значения другого итерируемого объекта для индикации того, следует
# ли принять значение или игнорировать его
from itertools import compress, cycle

every_third = cycle([False, False, True])
data = range(1, 10)
for i in compress(data, every_third):
    print(i, end=' ')
print()
