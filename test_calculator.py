import pytest
from calculator import Calculator


@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-5, 5, 0),
    (1.5, 2.5, 4.0),
    (-10, -20, -30),
    (100, 0.001, 100.001),
])
def test_add_parametrized(calc, a, b, expected):
    """Параметризованный тест для add — граничные и типичные значения."""
    result = calc.add(a, b)
    if isinstance(expected, float):
        assert abs(result - expected) < 1e-9
    else:
        assert result == expected


@pytest.mark.parametrize("a,b,expected", [
    (10, 3, 7),
    (3, 10, -7),
    (0, 5, -5),
    (5, 0, 5),
    (-3, -7, 4),
    (2.5, 1.0, 1.5),
])
def test_subtract_parametrized(calc, a, b, expected):
    """Параметризованный тест для subtract."""
    result = calc.subtract(a, b)
    if isinstance(expected, float):
        assert abs(result - expected) < 1e-9
    else:
        assert result == expected


@pytest.mark.parametrize("a,b,expected", [
    (3, 4, 12),
    (0, 100, 0),
    (-3, -4, 12),
    (3, -4, -12),
    (2.5, 4.0, 10.0),
    (0.1, 0.2, 0.02),
])
def test_multiply_parametrized(calc, a, b, expected):
    """Параметризованный тест для multiply."""
    result = calc.multiply(a, b)
    if isinstance(expected, float):
        assert abs(result - expected) < 1e-9
    else:
        assert result == expected


@pytest.mark.parametrize("a,b,expected", [
    (10, 2, 5),
    (7, 2, 3.5),
    (-10, -2, 5),
    (10, -2, -5),
    (0, 5, 0),
    (1.0, 4.0, 0.25),
])
def test_divide_parametrized(calc, a, b, expected):
    """Параметризованный тест для divide — включая дробные числа."""
    result = calc.divide(a, b)
    if isinstance(expected, float):
        assert abs(result - expected) < 1e-9
    else:
        assert result == expected


@pytest.mark.parametrize("a", [1, 5, 100, -7, 0.5])
def test_divide_by_zero_raises(calc, a):
    """Параметризованный тест: деление на ноль всегда выбрасывает ValueError."""
    with pytest.raises(ValueError):
        calc.divide(a, 0)


@pytest.fixture
def calc():
    """Fixture для создания экземпляра Calculator."""
    return Calculator()


class TestCalculatorAdd:
    """Тесты для метода add."""

    def test_add_positive_numbers(self, calc):
        """Тест сложения положительных чисел."""
        assert calc.add(2, 3) == 5

    def test_add_negative_numbers(self, calc):
        """Тест сложения отрицательных чисел."""
        assert calc.add(-2, -3) == -5

    def test_add_mixed_numbers(self, calc):
        """Тест сложения положительного и отрицательного чисел."""
        assert calc.add(5, -3) == 2

    def test_add_zeros(self, calc):
        """Тест сложения с нулем."""
        assert calc.add(0, 0) == 0

    def test_add_floats(self, calc):
        """Тест сложения дробных чисел."""
        assert abs(calc.add(1.5, 2.5) - 4.0) < 1e-9


class TestCalculatorSubtract:
    """Тесты для метода subtract."""

    def test_subtract_positive_numbers(self, calc):
        """Тест вычитания положительных чисел."""
        assert calc.subtract(10, 3) == 7

    def test_subtract_negative_result(self, calc):
        """Тест вычитания с отрицательным результатом."""
        assert calc.subtract(3, 10) == -7

    def test_subtract_zeros(self, calc):
        """Тест вычитания нуля."""
        assert calc.subtract(5, 0) == 5

    def test_subtract_from_zero(self, calc):
        """Тест вычитания из нуля."""
        assert calc.subtract(0, 5) == -5


class TestCalculatorMultiply:
    """Тесты для метода multiply."""

    def test_multiply_positive_numbers(self, calc):
        """Тест умножения положительных чисел."""
        assert calc.multiply(3, 4) == 12

    def test_multiply_by_zero(self, calc):
        """Тест умножения на ноль."""
        assert calc.multiply(5, 0) == 0

    def test_multiply_negative_numbers(self, calc):
        """Тест умножения отрицательных чисел."""
        assert calc.multiply(-3, -4) == 12

    def test_multiply_mixed_signs(self, calc):
        """Тест умножения чисел с разными знаками."""
        assert calc.multiply(3, -4) == -12

    def test_multiply_floats(self, calc):
        """Тест умножения дробных чисел."""
        assert abs(calc.multiply(2.5, 4.0) - 10.0) < 1e-9


class TestCalculatorDivide:
    """Тесты для метода divide."""

    def test_divide_positive_numbers(self, calc):
        """Тест деления положительных чисел."""
        assert calc.divide(10, 2) == 5

    def test_divide_with_remainder(self, calc):
        """Тест деления с остатком."""
        assert abs(calc.divide(7, 2) - 3.5) < 1e-9

    def test_divide_by_zero_raises_error(self, calc):
        """Тест деления на ноль должен выбрасывать ValueError."""
        with pytest.raises(ValueError):
            calc.divide(5, 0)

    def test_divide_negative_numbers(self, calc):
        """Тест деления отрицательных чисел."""
        assert calc.divide(-10, -2) == 5

    def test_divide_mixed_signs(self, calc):
        """Тест деления чисел с разными знаками."""
        assert calc.divide(10, -2) == -5
