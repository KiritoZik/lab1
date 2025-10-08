from src.tokenizer import tokenizer
from src.parser import expr
from src.constants import ERROR_COMBINATION, ALL_OPERATORS
from src.errors import (CountBracketError, NullBracketError,
                        InvalidCharacterError, FirstBracketError, NullExpressionError,
                        LotOperatorError, LastOperatorError, FirstOperatorError,
                        SeamBracketsError, LotPointError, NotOperatorError)

def calculate(expression: str) -> float:
    """
    :param expression:
    :return:
    """
    if '()' in expression:
        raise NullBracketError("Скобки не могут быть пустыми")

    tokens = tokenizer(expression)

    if all(ch not in ALL_OPERATORS for ch in tokens):
        raise NotOperatorError("Нет операторов")

    str_tokens = ''.join(tokens)
    if any(op in str_tokens for op in ERROR_COMBINATION):
        raise LotOperatorError("Два оператора не могут стоять подряд")

    if ')(' in str_tokens:
        raise SeamBracketsError("Между скобками должен быть оператор")

    if '..' in expression:
        raise LotPointError("Более одной запятой подряд быть не может\n")

    if tokens[-1] in ALL_OPERATORS:
        raise LastOperatorError("Выражение не может оканчиваться не числом/скобками")

    if (tokens[0] not in '+-') and (tokens[0] in ALL_OPERATORS):
        raise FirstOperatorError("Бинарный оператор не может стоять в начале выражения")

    if tokens.count('(') != tokens.count(')'):
        raise CountBracketError("Количество открывающих и закрывающих скобок не равно")

    for index in range(len(tokens)):
        try:
            tokens[index] = float(tokens[index])
        except ValueError:
            if (tokens[index] not in ALL_OPERATORS) and (tokens[index] not in '()'):
                raise InvalidCharacterError("Введен недопустимый символ")

    if tokens[0] in ')':
        raise FirstBracketError("Закрывающая скобка не может стоять в начале")

    if not tokens:
        raise NullExpressionError("Введена пустая строка")

    return expr(tokens)
