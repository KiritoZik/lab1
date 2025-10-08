from src.constants import OPERATORS_ADD, OPERATORS_MUL, OPERATORS_POW, UNARY_OPERATORS, ERROR_COMBINATION


'''Основная функция для вычисления значения выражения, \
с которого начинается рекурсивный спуск'''
def parse_expression(tokens: list) -> float:
    if any(op in ''.join(tokens) for op in ERROR_COMBINATION):
        raise SyntaxError("ERROR")
    now_token_index = 0
    for index in range(len(tokens)):
        token = tokens[index]
        try:
            tokens[index] = float(token)
        except ValueError:
            continue
    result, now_token_index = add_function(tokens, now_token_index)
    if now_token_index != len(tokens):
        raise ValueError("ERROR")
    return result


# Функция
def add_function(tokens: list, now_token_index: int) -> tuple[float, int]:
    left_token, now_token_index = mul_function(tokens, now_token_index)
    while now_token_index < len(tokens) and tokens[now_token_index] in OPERATORS_ADD:
        operation = tokens[now_token_index]
        now_token_index += 1
        right_token, now_token_index = mul_function(tokens, now_token_index)
        left_token = add_operation(left_token, operation, right_token)
    return left_token, now_token_index


def mul_function(tokens: list, now_token_index: int) -> tuple[float, int]:
    left_token, now_token_index = power_function(tokens, now_token_index)
    while now_token_index < len(tokens) and tokens[now_token_index] in OPERATORS_MUL:
        operator = tokens[now_token_index]
        now_token_index += 1
        right_token, now_token_index = power_function(tokens, now_token_index)
        if operator == '*':
            left_token = mul_operation_float(left_token, operator, right_token)
        if operator == '/':
            if right_token != 0.0:
                left_token = mul_operation_float(left_token, operator, right_token)
            else:
                raise ZeroDivisionError("ДЕЛЕНИЕ НА НОЛЬ")
        if operator == '//' or operator == '%':
            if not right_token.is_integer() or not left_token.is_integer():
                raise TypeError("ТОЛЬКО ДЛЯ ЦЕЛЫХ")
            left_token =float(mul_operation_integer(int(left_token), operator, int(right_token)))

    return left_token, now_token_index


def power_function(tokens: list, now_token_index: int) -> tuple[float, int]:
    left_token, now_token_index = unary_function(tokens, now_token_index)
    if  now_token_index < len(tokens):
        if tokens[now_token_index] in OPERATORS_POW:
            now_token_index += 1
            right_token, now_token_index = power_function(tokens, now_token_index)
            left_token = left_token ** right_token
    return left_token, now_token_index


def unary_function(tokens: list, now_token_index: int) -> tuple[float,int]:
    if tokens[now_token_index] in UNARY_OPERATORS:
        unary = tokens[now_token_index]
        now_token_index += 1
        digit, now_token_index = primary_function(tokens, now_token_index)
        if unary == '+':
            return digit, now_token_index
        elif unary == '-':
            return -digit, now_token_index

    return primary_function(tokens, now_token_index)


def primary_function(tokens: list, now_token_index: int) -> tuple[float, int]:
    now_token = tokens[now_token_index]
    if now_token == '(':
        now_token_index += 1
        result, now_token_index = add_function(tokens, now_token_index)
        if (len(tokens) <= now_token_index) or tokens[now_token_index]  != ')':
            raise ValueError("СКОБКИ НЕ ЗАКРЫТЫ")
        now_token_index += 1
        return result, now_token_index
    else:
        try:
            result = float(tokens[now_token_index])
        except ValueError:
            raise ValueError("ERROR")

    return result, now_token_index+1


def mul_operation_float(left_token: float, operator, right_token: float) -> float:
    if operator == '*': return left_token * right_token
    else: return left_token / right_token


def mul_operation_integer(left_token: int, operator, right_token: int) -> int:
    if operator == '//': return left_token // right_token
    else: return left_token % right_token


def add_operation(left_token, operation, right_token) -> float:
    if operation == '+': return left_token + right_token
    else: return left_token - right_token

