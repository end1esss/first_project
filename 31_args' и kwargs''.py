a, b, *c = [1, True, 4, 6, 'hello ', 7, 9]
# 1 True [4, 6, 'hello ', 7, 9]

a, *b, c = 'hello moto'
# 2 h ['e', 'l', 'l', 'o', ' ', 'm', 'o', 't'] o

s = [4, 10]
print(list(range(*s)))
# 3 [4, 5, 6, 7, 8, 9]


def f(a, b, c, d):
    print(a, b, c, d)


a = (True, 71, 'hi', [1, 2, 3])
f(*a)
# а раскроется и передадутся все значения


def f(*args):
    print(args)


f(1, 2, 3, 4, 5, 6)
# передаём произвольное кол-во элементов  в функции


def f(**kwargs):
    print(kwargs)


f(a=1, b=2, c=3)
# {'a': 1, 'b': 2, 'c': 3}

*a, b = 'qweqweqweqwe '
