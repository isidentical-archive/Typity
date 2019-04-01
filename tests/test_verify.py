import pytest
import typing
from typity.verify import verify

def test_verify_basic():
    @verify
    def add(x: int, y: int):
        pass
    
    add(3, 2)
    with pytest.raises(TypeError):
        add("a", "b")

def test_verify_basic_return():
    @verify
    def add(x: int, y: int) -> int:
        pass
    
    add(3, 2)
    with pytest.raises(TypeError):
        add("a", "b")
        
def test_verify_union():
    @verify
    def add(x: typing.Union[int, str], y: int) -> int:
        pass
    
    add("a", 2)
    with pytest.raises(TypeError):
        add(b"a", "b")


def test_verify_list():
    @verify
    def add(x: typing.List[int], y: int) -> int:
        pass
    
    add([3], 2)
    with pytest.raises(TypeError):
        add(1, 2)
