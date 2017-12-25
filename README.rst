https://www.kancloud.cn/lanyulei/python/357718

http://blog.51cto.com/xiexiaojun/1939995


https://github.com/sh4nks/flask-caching/blob/master/flask_caching/__init__.py


https://github.com/argaen/aiocache/blob/master/aiocache/decorators.py


解包， 把所有参数复制到对应名字的变量，

参考 functools的_make_key生成 hash_key

functools中：

    @recursive_repr()
    def __repr__(self):
        qualname = type(self).__qualname__
        args = [repr(self.func)]
        args.extend(repr(x) for x in self.args)
        args.extend(f"{k}={v!r}" for (k, v) in self.keywords.items())
        if type(self).__module__ == "functools":
            return f"functools.{qualname}({', '.join(args)})"
        return f"{qualname}({', '.join(args)})"

