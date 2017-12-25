# -*- coding: utf-8 -*-
import functools
import inspect
from inspect import Parameter

def mydec(func):
    @functools.wraps(func)
    def w(*args, **kw):
        print('---' * 20)
        print(args, kw)
        x = inspect.signature(func)
        print('this is str(x)', str(x))
        data = {}
        for i, p in enumerate(x.parameters.values()):
            print(i, p, p.kind)
            if p.kind == Parameter.POSITIONAL_OR_KEYWORD:
                data[p.name] = args[i]
            elif p.kind == Parameter.VAR_POSITIONAL:
                data[p.name] = args[i:]
            elif p.kind == Parameter.KEYWORD_ONLY:
                data[p.name] = p.default
        data.update(kw)
        print('this is data', data)
        return func(*args, **kw)
    return w


@mydec
def hello(a, a2, *args, b=2, c=None, **kw):
    print(a, b, c)

# print('1' * 30)
# print(hello(1, 2))
# 
# print('2' * 30)
# print(hello(1, b=2))

print('3' * 30)
print(hello(11, 12, 13, 14, c=2, z=222))

