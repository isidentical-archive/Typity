# Typity
Typing Tools

## Example
### Annotate
```py
from typity.annotate import annotate

assert (
    annotate({"a": [1, 2, "abc"], "c": b"ddd"})
    is typing.Dict[str, typing.Union[bytes, typing.List[typing.Union[str, int]]]]
)
```
### Basic Resolving
```py
from typity.resolve import resolve
assert r.dispatch(typing.Union[typing.List[int], typing.Tuple[str]], [15, 30])
```
