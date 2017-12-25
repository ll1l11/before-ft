# -*- coding: utf-8 -*-
from functools import wraps

def qn(func):
    @wraps(func)
    def w(*args, **kw):
        print(func.__name__)
        print(func.__qualname__)
        return func(*args, **kw)
    return w


class Cat:
    @qn
    def hello(self, name):
        print('hello', name)


c = Cat()
c.hello('abc')
