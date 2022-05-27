import copy
import functools


@functools.total_ordering
class MyClass:
    """functools.total_ordering - Настраивает все методы сравнения"""
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return self.name > other.name

    def __repr__(self):
        return self.name


if __name__ == '__main__':
    a = MyClass('hello')
    my_list = [a]
    dup = copy.copy(my_list)

    print('     my_list:', my_list)
    print('     dup:', dup)
    print('     dup is my_list:', (dup is my_list))
    print('     dup == my_list:', (dup == my_list))
    print('     dup[O] is my_list[0]:', (dup[0] is my_list[0]))
    print('     dup[O] == my_list[0]:', (dup[0] == my_list[0]))
