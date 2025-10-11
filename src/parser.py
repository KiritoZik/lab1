from src.constants import OPERATORS_ADD, OPERATORS_MUL, OPERATORS_POW, UNARY_OPERATORS
from src.errors import IntegerOperationError
from src.errors import NegativeSqrtError


def expr(tokens: list) -> float:
    """
    Начало рекурсивного спуска
    :param tokens: список токенов
    :return: возвращает значение арифметического выражения.
    """
    now_token_index = 0
    result, now_token_index = add(tokens, now_token_index)
    if now_token_index != len(tokens):
        raise ValueError("Неверный ввод")
    return result


def add(tokens: list, now_token_index: int) -> tuple[float, int]:
    """
    Реализация операции сложения и вычитания арифметических выражений
    :param tokens: список токенов
    :param now_token_index: индекс текущего токена
    :return: кортеж из двух элементов. Первый -- значение определенного куска выражения, а второй -- текущий индекс токена.
    """
    left_token, now_token_index = mul(tokens, now_token_index)
    while (now_token_index < len(tokens)
               and tokens[now_token_index] in OPERATORS_ADD):
        operation = tokens[now_token_index]
        now_token_index += 1
        right_token, now_token_index = mul(tokens, now_token_index)
        left_token = OPERATORS_ADD[operation](left_token, right_token)
    return left_token, now_token_index



def mul(tokens: list, now_token_index: int) -> tuple[float, int]:
    """
    Реализация операций умножения, деления, целочисленного деления и остатка от деления на целое число арифметического выражения
    :param tokens: список токенов
    :param now_token_index: индекс текущего токена
    :return: кортеж из двух элементов. Первый -- значение определенного куска выражения, а второй -- текущий индекс токена.
    """
    left_token, now_token_index = power(tokens, now_token_index)
    while ((now_token_index < len(tokens))
                and (tokens[now_token_index] in OPERATORS_MUL)):
        operator = tokens[now_token_index]
        now_token_index += 1
        right_token, now_token_index = power(tokens, now_token_index)
        if operator == '*':
            left_token = OPERATORS_MUL[operator](left_token, right_token)
        if operator == '/':
            if right_token != 0.0:
                left_token = OPERATORS_MUL[operator](left_token, right_token)
            else:
                raise ZeroDivisionError("Деление на ноль карается Битюковым ")
        if operator in ('//', '%'):
            if right_token == 0.0:
                raise ZeroDivisionError("Деление на ноль карается Битюковым")
            if (not right_token.is_integer()) or (not left_token.is_integer()):
                raise IntegerOperationError(f"Операция {operator} только для целых чисел")
            left_token =float(OPERATORS_MUL[operator](int(left_token), int(right_token)))

    return left_token, now_token_index


def power(tokens: list, now_token_index: int) -> tuple[float, int]:
    """
    Реализация операции возведения в степень
    :param tokens: список токенов
    :param now_token_index: индекс текущего токена
    :return: кортеж из двух элементов. Первый -- значение определенного куска выражения, а второй -- текущий индекс токена.
    """
    left_token, now_token_index = unary(tokens, now_token_index)
    if  now_token_index < len(tokens):
        if tokens[now_token_index] in OPERATORS_POW:
            operator = tokens[now_token_index]
            now_token_index += 1
            right_token, now_token_index = power(tokens, now_token_index)
            left_token = OPERATORS_POW[operator](left_token, right_token)
            if isinstance(left_token, complex):
                raise NegativeSqrtError("Из отрицательного числа нельзя извлечь корень четной степени")
    return left_token, now_token_index


def unary(tokens: list, now_token_index: int) -> tuple[float,int]:
    """
    Реализация определения унарных знаков у чисел
    :param tokens: список токенов
    :param now_token_index: индекс текущего элемента
    :return: кортеж из двух элементов. Первый -- значение определенного куска выражения (число с унарным знаком, просто число), а второй -- текущий индекс токена.
    """
    if tokens[now_token_index] in UNARY_OPERATORS:
        unary_mark = tokens[now_token_index]
        now_token_index += 1
        digit, now_token_index = primary(tokens, now_token_index)
        if unary_mark == '+':
            return digit, now_token_index
        elif unary_mark == '-':
            return -digit, now_token_index

    return primary(tokens, now_token_index)


def primary(tokens: list, now_token_index: int) -> tuple[float, int]:
    """
    Реализация определения выражений в скобках, числа
    :param tokens: список токенов
    :param now_token_index: индекс текущего токена
    :return: кортеж из двух элементов. Первый -- значение определенного куска выражения (просто число), а второй -- текущий индекс токена.
    """
    now_token = tokens[now_token_index]
    if now_token == '(':
        now_token_index += 1
        result, now_token_index = add(tokens, now_token_index)
        now_token_index += 1
        return result, now_token_index
    else:
        result = float(tokens[now_token_index])
    return result, now_token_index+1
