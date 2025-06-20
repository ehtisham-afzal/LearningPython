import pytest
from distances import convert_au_to_m


def test_with_int():
    assert convert_au_to_m(1) == 149597870700
    assert convert_au_to_m(50) == 7479893535000


def test_with_float():
    assert convert_au_to_m(0.001) == pytest.approx(149597870.691, abs=1e-2)


def test_with_string():
    with pytest.raises(TypeError):
        convert_au_to_m("1")
