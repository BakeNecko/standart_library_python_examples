# Поскольку значения, возвращаемые функцией time (), основаны на показаниях
# системных часов, которые могут быть изменены пользователем или системными
# службами для синхронизации часов на нескольких компьютерах, результат
# каждого из повторных измерений, получаемых c ее помощью, может отличаться
# от предыдущего как в одну, так и в другую сторону. Это может приводить к
# неожиданному поведению результатов при попытках измерения длительностей временных
# промежутков или использования их для других целей. Этого можно избежать,
# используя функцию monotonic (), последовательные вызовы которой возвращают
# только возрастающие значения.
import time

start = time.monotonic()
time.sleep(0.1)
end = time.monotonic()
print('start: {:>9.2f}'.format(start))
print('end  : {:>9.2f}'.format(end))
print('span : {:9.2f}'.format(start-end))

# Для монотонных часов начало отсчета не определено, поэтому возвращаемые
# ими значения полезны лишь для выполнения вычислений совместно со значениями
# других часов. В данном примере функция monotonic () используется для измерения
# длительности паузы.
