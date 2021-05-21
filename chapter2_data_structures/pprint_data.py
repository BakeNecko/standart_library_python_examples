import pprint
import logging

data = [
    (1, {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}),
    (2, {'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L'}),
    (3, ['m', 'n']),
    (4, ['o', 'p', 'q']),
    (5, ['r', 's', 't', 'u', 'v', 'x', 'y', 'z'])
]
#
# print('PRINT:')
# print(data)
# print()
# print('PPRINT:')
# pprint.pprint(data)
###########################################
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(levelname)-8s %(message)s'
# )
# logging.debug('Logging pformatted data')
# formatted = pprint.pformat(data)
# for line in formatted.splitlines():
#     logging.debug(line.rstrip())
###########################################
# class node:
#     def __init__(self, name, contents=[]):
#         self.name = name
#         self.contents = contents
#
#     def __repr__(self):
#         return (
#             'node(' + repr(self.name) + ', ' +
#             repr(self.contents) + ')'
#         )
#
#
# trees = [
#     node('node-1'),
#     node('node-2', [node('node-2-1')]),
#     node('node-3', [node('node-3-1')]),
# ]
#
# pprint.pprint(trees)
#############################################
# pprint.pprint(data, depth=1)
# pprint.pprint(data, depth=2)
#############################################
# for width in [80, 5]:
#     print('WIDTH =', width)
#     pprint.pprint(data, width=width)
#     print()
#############################################
print('DEFAULT:')
pprint.pprint(data, compact=False)
print('\nCOMPACT:')
pprint.pprint(data, compact=True)
