class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        # Геттер для температуры в градусах Цельсия
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        # Сеттер для температуры в градусах Цельсия с валидацией
        if not isinstance(value, (int, float)):
            raise ValueError("Температура должна быть числом")
        self._celsius = value

    @property
    def fahrenheit(self):
        # Динамическое свойство для температуры в градусах Фаренгейта
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        # Сеттер для температуры в градусах Фаренгейта
        if not isinstance(value, (int, float)):
            raise ValueError("Температура должна быть числом")
        self._celsius = (value - 32) * 5 / 9