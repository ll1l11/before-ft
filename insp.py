# -*- coding: utf-8 -*-
import functools
import inspect

def mydec(func):
    @functools.wraps(func)
    def w(*args, **kw):
        print('hahah')
        print(args, kw)
        x = inspect.signature(func)
        print('x', x, type(x))
        return func(*args, **kw)
    return w


@mydec
def hello(a, b=2, c=None):
    print(a, b, c)

print('1' * 30)
print(hello(1, 2))

print('2' * 30)
print(hello(1, b=2))

print('3' * 30)
print(hello(a=1, c=2))
