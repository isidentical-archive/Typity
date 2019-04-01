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
from typity.resolver import Resolver
r = Resolver()
assert r.dispatch(typing.Union[typing.List[int], typing.Tuple[str]], [15, 30])
```

### Verifiying Types at Runtime
```py
from typity.verify import verify
@verify
def add(x: typing.List[int], y: int) -> int:
    pass

add([3], 2)
with pytest.raises(TypeError):
    add(1, 2)
```
