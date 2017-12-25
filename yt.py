# -*- coding: utf-8 -*-
import inspect


def function_params_to_dict(func, args, kw):
    """将func的参数和默认参数封装到一个dict中去"""
    kw = kw.copy()
    sig = inspect.signature(func)
    result = {}
    for i, p in enumerate(sig.parameters.values()):
        print(i, p, p.kind)
        if p.kind == inspect.Parameter.POSITIONAL_OR_KEYWORD:
            if len(args) > i:
                result[p.name] = args[i]
            else:
                result[p.name] = kw.pop(p.name)
        elif p.kind == inspect.Parameter.VAR_POSITIONAL:
            result[p.name] = args[i:]
        elif p.kind == inspect.Parameter.KEYWORD_ONLY:
            result[p.name] = p.default
        elif p.kind == inspect.Parameter.VAR_KEYWORD:
            result[p.name] = kw
    print('this is kw', kw)
    print('this is result', result)
    return result


def md(func):
    def w(*args, **kw):
        print('begin', args, kw)
        print(function_params_to_dict(func, args, kw))
        print('end', args, kw)
        return func(*args, **kw)
    return w


@md
def f3(a, b, c=3, **kw):
    print(a, b, c, kw)
    pass


# r = function_params_to_dict(f3, [], dict(a=1, b=5, c=7))
f3(1, b=2, c=7, x=5)
