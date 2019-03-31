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
