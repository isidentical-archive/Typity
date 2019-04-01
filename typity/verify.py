from functools import wraps
from typity.resolver import Resolver
from typity.annotate import annotate


def verify(func):
    resolver = Resolver()
    @wraps(func)
    def wrapper(*args, **kwargs):
        args = list(args)
        args.extend(kwargs.values())

        spec = func.__annotations__
        spec.pop("return", 0)
        spec = spec.values()

        for given, expected in zip(args, spec):
            if not resolver.dispatch(expected, given):
                expected = (
                    expected.__name__ if hasattr(expected, "__name__") else expected
                )
                given = (
                    annotate(given).__name__
                    if hasattr(annotate(given), "__name__")
                    else annotate(given)
                )
                raise TypeError(
                    f"Invalid argument type; expected {expected}, got {given}"
                )

        return func(*args, **kwargs)

    return wrapper
