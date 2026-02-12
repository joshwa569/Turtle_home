
import main
import inspect

def test_functions_exist():
    assert hasattr(main, "draw_square")
    assert hasattr(main, "draw_triangle")
    assert hasattr(main, "draw_house")

def test_square_logic():
    source = inspect.getsource(main.draw_square)
    assert "90" in source
    assert "for" in source or "while" in source

def test_triangle_logic():
    source = inspect.getsource(main.draw_triangle)
    assert "120" in source
    assert "for" in source or "while" in source

def test_house_calls():
    source = inspect.getsource(main.draw_house)
    assert "draw_square" in source
    assert "draw_triangle" in source
