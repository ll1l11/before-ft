# -*- coding: utf-8 -*-
import functools
import inspect

def mydec(func):
    @functools.wraps(func)
    def w(*args, **kw):
        print('@@@' * 20)
        print(dir(func))
        print(repr(func))
        print(func.__module__)
        print(func.__annotations__)
        print(args, kw)
        x = inspect.signature(func)
        print('this is str(x)', str(x))
        print(dir(x.parameters))
        for name in x.parameters:
            p = x.parameters[name]
            # print(p, type(p))
            print(p.name, p.default, p.kind, p.annotation)
        for i, p in enumerate(x.parameters.values()):
            print(i, p, type(p))
        for i, p in enumerate(x.parameters):
            print(i, p, type(p))
        for m, n in x.parameters.items():
            print(m, n)
        print('x', x, type(x), dir(x))
        return func(*args, **kw)
    return w


@mydec
def hello(a, *args, b=2, c=None, **kw):
    print(a, b, c)

# print('1' * 30)
# print(hello(1, 2))
# 
# print('2' * 30)
# print(hello(1, b=2))

print('3' * 30)
print(hello(11, 12, 13, 14, c=2, z=222))

