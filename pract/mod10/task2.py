import re

def is_valid_color(color_string):
    """
    Проверяет, является ли входная строка корректной записью цвета в одном из трех web форматов: rgb, hex, hsl.

    >>> is_valid_color('#21f48D')
    True
    >>> is_valid_color('#888')
    True
    >>> is_valid_color('rgb(255, 255, 255)')
    True
    >>> is_valid_color('rgb(10%, 20%, 0%)')
    True
    >>> is_valid_color('hsl(200, 100%, 50%)')
    True
    >>> is_valid_color('hsl(0, 0%, 0%)')
    True

    >>> is_valid_color('#2345')
    False
    >>> is_valid_color('ffffff')
    False
    >>> is_valid_color('rgb(257, 50, 10)')
    False
    >>> is_valid_color('hsl(20, 10, 0.5)')
    False
    >>> is_valid_color('hsl(34%, 20%, 50%)')
    False
    """
    # Регулярное выражение для rgb формата
    rgb_pattern = re.compile(r'^rgb\((\d{1,3}%?)[, ]\s*(\d{1,3}%?)[, ]\s*(\d{1,3}%?)\)$')

    # Регулярное выражение для hex формата
    hex_pattern = re.compile(r'^#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})$')

    # Регулярное выражение для hsl формата
    hsl_pattern = re.compile(r'^hsl\((\d{1,3})[, ]\s*(\d{1,3}%)[, ]\s*(\d{1,3}%)\)')

    # Проверка соответствия rgb формату
    # Регулярное выражение для rgb формата
    rgb_pattern = re.compile(r'^rgb\((\d{1,3}%?)[, ]\s*(\d{1,3}%?)[, ]\s*(\d{1,3}%?)\)$')

    # Регулярное выражение для hex формата
    hex_pattern = re.compile(r'^#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})$')

    # Регулярное выражение для hsl формата
    hsl_pattern = re.compile(r'^hsl\((\d{1,3})[, ]\s*(\d{1,3}%)[, ]\s*(\d{1,3}%)\)$')

    # Проверка соответствия rgb формату
    if rgb_match := rgb_pattern.match(color_string):
        # Проверка диапазона значений для rgb
        if all(0 <= int(value.rstrip('%')) <= 255 for value in rgb_match.groups()):
            return True

    # Проверка соответствия hex формату
    if hex_pattern.match(color_string):
        return True

    # Проверка соответствия hsl формату
    if hsl_pattern.match(color_string):
        return True

    # Возвращаем False, если строка не соответствует ни одному из форматов
    return False


# Запуск doctests
if __name__ == "__main__":
    import doctest
    result = doctest.testmod()

    if result.failed == 0:
        print("Все тесты прошли успешно!")
    else:
        print("Тесты не прошли.")

