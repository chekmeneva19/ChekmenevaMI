import re

def is_valid_password(password):
    """
    Проверяет, соответствует ли входной пароль всем заданным ограничениям.

    >>> is_valid_password("rtG3FG!Tr^e")
    True

    >>> is_valid_password("aA1!*!1Aa")
    True

    >>> is_valid_password("oF^a1D@y5e6")
    True

    >>> is_valid_password("enroi#$rkdeR#$092uWedchf34tguv394h")
    True

    >>> is_valid_password("пароль")
    False

    >>> is_valid_password("password")
    False

    >>> is_valid_password("qwerty")
    False

    >>> is_valid_password("lOngPa$$$W0Rd")
    False
    """

    # Пароль должен содержать только латинские символы, цифры и специальные символы ^$%@#&*!?
    if not re.match(r'^[a-zA-Z0-9^$%@#&*!?]+$', password):
        return False

    # Пароль должен состоять из не менее чем шести символов
    if len(password) < 6:
        return False

    # Пароль должен содержать по крайней мере два латинских символа в верхнем регистре
    if len(re.findall(r'[A-Z]', password)) < 2:
        return False

    # Пароль должен содержать по крайней мере одну цифру
    if len(re.findall(r'[0-9]', password)) < 1:
        return False

    # Пароль должен содержать по крайней мере два различных специальных символа
    if len(set(re.findall(r'[^a-zA-Z0-9]', password))) < 2:
        return False

    # Пароль не должен содержать трех одинаковых символов подряд
    if re.search(r'([a-zA-Z0-9^$%@#&*!?])\1\1', password):
        return False

    return True

if __name__ == "__main__":
    import doctest
    result = doctest.testmod()

    if result.failed == 0:
        print("Все тесты прошли успешно!")
    else:
        print("Тесты не прошли.")

