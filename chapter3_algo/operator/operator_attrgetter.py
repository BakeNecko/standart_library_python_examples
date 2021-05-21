# attrgetter == lambda x,n='attrname': getattr(x,n)
from operator import attrgetter


class MyObj:
    def __init__(self, arg):
        super(MyObj, self).__init__()
        self.arg = arg

    def __repr__(self):
        return f'MyObj({self.arg})'


l = [MyObj(i) for i in range(5)]
print('objects: ', l)

g = attrgetter('arg')
vals = [g(i) for i in l]
print('arg values: ', vals)

# sort with attrgetter
l.reverse()
print('reversed: ', l)
print('sorted: ', sorted(l, key=g))
