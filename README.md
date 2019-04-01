# Typity
Typing Tools

## Example
### Annotate
[![asciicast](https://asciinema.org/a/a8CdzGCEpJVPaZSVJtTtatgGd.svg)](https://asciinema.org/a/a8CdzGCEpJVPaZSVJtTtatgGd)

```py
from typity.annotate import annotate

assert (
    annotate({"a": [1, 2, "abc"], "c": b"ddd"})
    is typing.Dict[str, typing.Union[bytes, typing.List[typing.Union[str, int]]]]
)
```

### Basic Resolving
[![asciicast](https://asciinema.org/a/b6H1dpgRzHyKKpgdUFN46sz7a.svg)](https://asciinema.org/a/b6H1dpgRzHyKKpgdUFN46sz7a)
```py
from typity.resolve import resolve
assert r.dispatch(typing.Union[typing.List[int], typing.Tuple[str]], [15, 30])
```
