import typing
from typity.annotate import annotate, Builtin


class Resolver:
    resolvers = {}

    def dispatch(self, expected, given):
        protocol = expected.__origin__ if hasattr(expected, "__origin__") else expected
        if self.resolvers.get(protocol):
            return self.resolvers[protocol](expected, given)
        else:
            return self.resolvers[None](expected, given)

    @classmethod
    def resolve(cls, typ):
        def wrapper(func):
            cls.resolvers[typ] = func
            return func

        return wrapper


@Resolver.resolve(typing.Union)
def resolve_union(typ, item):
    if annotate(item) is type(item):
        return isinstance(
            item,
            tuple(
                filter(
                    lambda item: isinstance(item, Builtin),
                    typ.__args__,
                )
            ),
        )
    else:
        subresolver = Resolver()
        result = any(
            filter(
                lambda ann: subresolver.dispatch(ann, item), typ.__args__
            )
        )

        return result
        
@Resolver.resolve(typing.Any)
def resolve_any(_, __):
    return True

@Resolver.resolve(None)
def resolve_all(typ, item):
    return annotate(item) == typ
