import typing

def transform(func):
    def wrapper(*args, **kwargs):
        ret = func.__annotations__.get('return')
        res = func(*args, **kwargs)
        if not ret or isinstance(ret, (typing._GenericAlias, typing._SpecialForm)):
            return res
        else:
            return ret(res)
    return wrapper
