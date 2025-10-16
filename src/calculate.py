from src.tokenizer import tokenizer, is_number
from src.parser import expr
from src.constants import ERROR_COMBINATION, ALL_OPERATORS
from src.errors import (CountBracketError, NullBracketError, \
                        InvalidCharacterError, NullExpressionError, \
                        LotOperatorError, LastOperatorError, FirstOperatorError, \
                        SeamBracketsError, LotPointError, NotOperatorError, \
                        UnderscoreError, NotNumberError)

def calculate(expression: str) -> float:
    """
    Функция, где происходит большая часть обработки ошибок и переход в начало рекурсивного спуска
    :param expression:
    :return: возвращает значение арифметического выражения
    """
    tokens = tokenizer(expression)

    if not tokens:
        raise NullExpressionError("Введена пустая строка")

    if all(not is_number(token) for token in tokens):
        raise NotNumberError("Нет числовых значений")

    expression = expression.replace(' ', '')

    if '()' in expression:
        raise NullBracketError("Скобки не могут быть пустыми")

    if any(op in expression for op in ERROR_COMBINATION):
        raise LotOperatorError("Два оператора и более не могут стоять подряд")

    if ')(' in expression:
        raise SeamBracketsError("Между скобками должен быть оператор")

    if '..' in expression:
        raise LotPointError("Более одной точки подряд быть не может")

    if tokens[-1] in ALL_OPERATORS:
        raise LastOperatorError("Выражение не может оканчиваться не числом/скобками")

    if (tokens[0] not in '+-') and (tokens[0] in ALL_OPERATORS):
        raise FirstOperatorError("Бинарный оператор не может стоять в начале выражения")

    if tokens.count('(') != tokens.count(')'):
        raise CountBracketError("Количество открывающих и закрывающих скобок не равно")

    if all(ch not in ALL_OPERATORS for ch in tokens) or (tokens[0] in '+-' and len(tokens) == 2):
        raise NotOperatorError("Нет бинарных операторов")

    for index in range(len(tokens)):
        if (tokens[index] not in ALL_OPERATORS) and (tokens[index] not in '()_'):
            try:
                tokens[index] = float(tokens[index])
            except ValueError:
                raise InvalidCharacterError(f"Введен недопустимый символ: {tokens[index]}")

    all_index = [index for index in range(len(tokens)) if tokens[index] == "_"]
    if (str(tokens[0]) in '_' or str(tokens[-1]) in '_'
            or any( (type(tokens[index - 1]) is float) or (type(tokens[index + 1]) is float) for index in all_index) ):
        raise UnderscoreError("Нижнее подчеркивание должно стоять между числами числа")


    expression = expression.replace('_', '')
    tokens = tokenizer(expression)

    result = expr(tokens)
    point_index = str(result).find('.')
    if len(str(result)[point_index+1:]) > 2:
        number = input("Полученный ответ имеет более двух разрядов после 'запятой'."
                       "Введите до какого знака после 'запятой' нужно округлить, или любой ввод, если округление не нужно\n")
        if number.isdigit():
            result = round(result, int(number))
    return result
