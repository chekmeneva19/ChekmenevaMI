def memoize(func):
    cache = { }
    def wrapped_func(*args):
        key = args
        if key in cache:
            return cache[key]
        value = func(*args)
        cache[args] = value
        return value
    wrapped_func.__name__= func.__name__
    wrapped_func.__doc__ = func.__doc__
    return wrapped_func

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
res = fibonacci(20)
print(res)