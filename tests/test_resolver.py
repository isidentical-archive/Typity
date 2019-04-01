import pytest
import typing
from typity.resolver import Resolver


@pytest.fixture
def r():
    return Resolver()


def test_resolver_basic(r):
    assert r.dispatch(int, 1)
    assert not r.dispatch(int, "abc")
    assert r.dispatch(str, "a1b")
    assert not r.dispatch(str, b"abc")


def test_resolve_any(r):
    assert r.dispatch(typing.Any, [1, {"a": "b"}])
    assert r.dispatch(typing.Any, 1)


def test_resolve_union_simple(r):
    assert r.dispatch(typing.Union[str, int], "abc")
    assert r.dispatch(typing.Union[str, int], 2323)
    assert r.dispatch(typing.Union[str, int, typing.Dict[str, typing.List[int]]], "a")


def test_resolve_union_complex(r):
    assert r.dispatch(typing.Union[typing.List[int], typing.Tuple[str]], [15, 30])
    assert not r.dispatch(typing.Union[typing.List[int], typing.Tuple[str]], [15, "a"])
    assert r.dispatch(typing.Union[typing.List[int], typing.Tuple[str]], ("a",))
    assert not r.dispatch(typing.Union[typing.List[int], typing.Tuple[str]], ("a", "b"))
    assert r.dispatch(
        typing.Union[typing.List[int], typing.Tuple[str], typing.Union[str, None]],
        ("a",),
    )
