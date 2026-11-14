# calculator.py
class Calculator:
    def add(self, a: float, b: float) -> float:
        """Возвращает сумму двух чисел."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Возвращает разность двух чисел (a - b)."""
        # ошибка: возвращает b - a вместо a - b
        return b - a

    def multiply(self, a: float, b: float) -> float:
        """Возвращает произведение двух чисел."""
        # ошибка: всегда возвращает 4 вместо произведения a и b
        return 4.0

    def divide(self, a: float, b: float) -> float:
        """Возвращает частное от деления a на b.
        При делении на ноль должен выбрасывать ValueError.
        """
        # ошибка: возвраща 0.0 при делении на ноль вместо выбрасывания исключения
        if b == 0:
            return 0.0
        return a / b
    