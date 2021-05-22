# 3.4.7.3
# Иногда при создании сложных контекстов полезно иметь возможность прекратить выполнение операции,
# если контекст не может быть создан, но при этом отложить выполнение завершающих операций по освобождению всех ресурсов
# до более позднего момента времени, если все они могут быть настроены надлежащим образом. Например,
# если для операции требуется несколько долгосрочных
# сетевых соединений, то, возможно, лучше всего вообще не начинать выполнение
# операции, если одно из соединений не удается установить. Однако, если могут
# быть открыты все соединения, то все они должны оставаться открытыми в течение более длительного периода времени,
# чем время жизни одного менеджера
# контекста. В подобных сценариях можно использовать метод pop_all () класса ExitStack.
# Метод pop_all() удаляет из стека, для которого он вызван, все менеджеры контекста и
# функции обратного вызова и возвращает новый стек, заполненный этими же менеджерами
# контекста и функциями обратного вызова. Метод lose () нового стека может быть вызван для освобождения ресурсов позже,
# когда будет удален исходный стек.
import contextlib
from contextlib_context_managers import *


def variable_stack(contexts: object):
    with contextlib.ExitStack() as stack:
        for c in contexts:
            stack.enter_context(c)
        # Вернуть метод close() новго стека в качестве
        # функции, освобождающей ресурсы
        return stack.pop_all().close
    # Явно вернуть значение None, указывающее на то, что
    # инициализировать объект ExitStack невозможно, но операции
    # по освобождению ресурсов уже выполненны
    return None


print('No errors:')
cleaner = variable_stack([
    HandleError(1),
    HandleError(2)
])
cleaner()

print('\nHandled error building context manager stack:')
try:
    cleaner = variable_stack([
        HandleError(1),
        ErrorOnEnter(2),
    ])
except RuntimeError as err:
    print(f'caught error {err}')
else:
    if cleaner is not None:
        cleaner()
    else:
        print('no cleaner returned')

print('\nUnhandled error building context manager stack')
try:
    cleaner = variable_stack([
        PassError(1),
        ErrorOnEnter(2)
    ])
except RuntimeError as err:
    print(f'caught error {err}')
else:
    if cleaner is not None:
        cleaner()
    else:
        print('no cleaner returned')
