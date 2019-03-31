import typing
from collections import deque, defaultdict
from collections.abc import Sequence, Mapping
from typity.annotate import annotate

class CustomType:
    def __init__(self, elements):
        self.elements = elements

    def __getitem__(self, item):
        return self.elements[item]

    def keys(self):
        return self.elements.keys()

    def values(self):
        return self.elements.values()

    def __len__(self):
        return len(self.elements)


def test_basic():
    assert annotate(5) is int
    assert annotate("abc") is str
    assert annotate(b"naber") is bytes

def test_builtin_sequence():
    assert (
        annotate([1, 2, 3, "abc", [1, 2]])
        is typing.List[typing.Union[str, int, typing.List[int]]]
    )
    assert annotate((1, "abc", 2)) is typing.Tuple[int, str, int]

def test_custom_sequence():
    CustomSequence = Sequence.register(CustomType)
    assert (
        annotate(CustomSequence([1, 2, 3, CustomSequence(["abc", 1, 2])]))
        is typing.Sequence[typing.Union[int, typing.Sequence[typing.Union[str, int]]]]
    )

def test_builtin_mapping():
    assert annotate({"a": "b", "c": "d"}) is typing.Dict[str, str]
    assert (
        annotate({"a": 1, 1: "c"})
        is typing.Dict[typing.Union[str, int], typing.Union[str, int]]
    )
    assert (
        annotate({"a": [1, 2, "abc"], "c": b"ddd"})
        is typing.Dict[str, typing.Union[bytes, typing.List[typing.Union[str, int]]]]
    )

def test_custom_mapping():
    CustomMapping = Mapping.register(CustomType)
    assert (
        annotate(CustomMapping({"naber": "merhaba", 331: CustomMapping({"wow": 23})}))
        is typing.Mapping[
            typing.Union[str, int], typing.Union[str, typing.Mapping[str, int]]
        ]
    )

def test_collections():
    assert annotate(deque()) is typing.Deque
    assert annotate(deque((1, 3, 5, "abc"))) is typing.Deque[typing.Union[str, int]]
    assert (
        annotate(defaultdict(list, {"baba": "merhaba"}))
        is typing.DefaultDict[str, typing.Union[str, typing.List]]
    )


