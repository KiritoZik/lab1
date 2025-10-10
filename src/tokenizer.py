import re


def tokenizer(expression: str) -> list:
    """
    Токенизация выражения, полученного от пользователя
    :param expression: выражение в виде строки
    :return:список из токенов
    """
    token_re = re.compile(r"""
        \s*
        (
            \d+(?:\.\d+)?         # число
          | \*\*                   # ** (обязательно раньше *)
          | //                       # //
          | \S              # любой не пробельный символ
        )
    """, re.VERBOSE)
    tokens = [m.group(1) for m in token_re.finditer(expression)]
    return tokens


def is_number(token: str) -> bool:
    """
    Проверка токена на числовое значение
    :param token: один токен
    :return: True (если токен -- числовое выражение) or False (если токен -- не числовое значение)
    """
    if re.match(r"""\d+(?:\.\d+)?""", token) is None:
        return token.isdigit()
    return True

