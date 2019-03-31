import typing
from abc import ABC
from collections.abc import *
from functools import wraps
from types import FunctionType


class _Container(Container):
    def __subclasscheck__(cls):
        return issubclass(cls, Container) and not issubclass(cls, (str, bytes))


class Builtin(ABC):
    def __subclasscheck__(cls):
        return cls.__module__ == "builtins"


class Collections(ABC):
    def __subclasscheck__(cls):
        return cls.__module__ == "collections"


def build_union(of):
    return typing.Union.__getitem__(tuple(set(of)))


def annotate(item):
    if isinstance(item, _Container):
        if isinstance(item, Mapping):
            if isinstance(item, (Builtin, Collections)):
                typ = getattr(typing, typing._normalize_alias[item.__class__.__name__])
            else:
                typ = typing.Mapping

            if len(item) == 0:
                return typ
            else:
                return typ[
                    build_union(map(annotate, item.keys())),
                    build_union(
                        map(
                            annotate,
                            list(item.values()) + [item.default_factory()]
                            if hasattr(item, "default_factory")
                            else item.values(),
                        )
                    ),
                ]

        elif isinstance(item, Sequence):
            if isinstance(item, (Builtin, Collections)):
                typ = getattr(typing, typing._normalize_alias[item.__class__.__name__])
            else:
                typ = typing.Sequence

            if len(item) == 0:
                return typ
            elif len(typ.__args__) == 1:
                return typ[build_union(map(annotate, item))]
            else:
                return typ.__getitem__(tuple(map(annotate, item)))
    elif isinstance(item, FunctionType):

        @wraps(item)
        def wrapper(*args, **kwargs):
            argset = list(args)
            argset.extend(kwargs.values())
            argset = list(map(annotate, argset))
            result = item(*args, **kwargs)
            retval = annotate(result)
            return typing.Callable[argset, retval]

        return wrapper

    else:
        return type(item)
