from typity.transform import transform

def test_transform_basic():
    @transform
    def add(x, y) -> str:
        return x + y
    
    assert type(add(3, 2)) is str
