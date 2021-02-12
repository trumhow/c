# a = [1, 2, 3, 4, 5, 6, 7]
# print(list(filter(lambda x: x > 2, a)))


# a = [1, 2, 3, 2]
# b = [2, 2, 2]
# print(list(map(lambda x, y: x+y, a, b)))


# from functools import reduce
# print(reduce(lambda x, y: x+y, [1, 2]))


a = {'a': 'aa', 'b': 'bb'}
print(dict(zip(a.values(), a.keys())))
