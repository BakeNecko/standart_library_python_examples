"""
Модуль weakref обеспечивает поддержку слабых ссылок на объекты.
Создание обычный сслыки приводит к увеличенияю счётчика ссылок на объект,
что препядствует его удалению сборщиком мусора.

Особенность слабой ссылки в том, что она позволяет ссылаться на объект,
не препядствуя его автоматическому удалению.
"""
import gc
import weakref
from pprint import pprint

gc.set_debug(gc.DEBUG_UNCOLLECTABLE)


class ExpensiveObject:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'ExpensiveObject({})'.format(self.name)

    def __del__(self):
        print('(Deleting {})'.format(self))


def demo(cache_factory):
    all_refs = {}
    print('CACHE TYPE:', cache_factory)
    cache = cache_factory()
    for name in ['one', 'two', 'three']:
        o = ExpensiveObject(name)
        cache[name] = o
        all_refs[name] = o
        del o
    print('all_refs =', end=' ')
    pprint(all_refs)
    print('\nBefore, cache contains:', list(cache.keys()))
    for name, value in cache.items():
        print('{} = {}'.format(name, value))
        del value
    print('\n Cleanup:')
    del all_refs
    gc.collect()
    print('\n After, cache contains:', list(cache.keys()))
    for name, value in cache.items():
        print('{} = {}'.format(name, value))
    print('demo returning')
    return

if __name__ == '__main__':

    demo(dict)
    print('#################')
    demo(weakref.WeakValueDictionary)