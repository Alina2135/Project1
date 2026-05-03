import pytest
from Pr1_Biriuk import calculate


# ========== 1. ФІКСТУРА ==========
@pytest.fixture
def test_data():
    return [("2+3", 5), ("10-5", 5), ("3*4", 12), ("8/2", 4)]


def test_with_fixture(test_data):
    for expr, expected in test_data:
        assert calculate(expr) == expected


# ========== 2. ПАРАМЕТРИЗАЦІЯ ==========
@pytest.mark.parametrize("expr, expected", [
    ("2+3", 5),
    ("10-5", 5),
    ("3*4", 12),
    ("8/2", 4),
])
def test_parametrized(expr, expected):
    assert calculate(expr) == expected


# ========== 3. pytest.raises ==========
def test_raises_zerodivision():
    with pytest.raises(ZeroDivisionError):
        calculate("5/0")


def test_raises_valueerror():
    with pytest.raises(ValueError):
        calculate("2+*3")


# ========== 4. @pytest.mark.skip ==========
@pytest.mark.skip(reason="Тимчасово пропущено")
def test_skipped():
    assert calculate("100-50") == 50


# ========== 5. @pytest.mark.xfail ==========
@pytest.mark.xfail(reason="Відомий дефект")
def test_xfail():
    assert calculate("1/0") == 0


# ========== 6. ПОМИЛКОВІ ТЕСТИ ==========
def test_broken_1():
    assert calculate("2+2") == 5


def test_broken_2():
    assert calculate("10/2") == 6