from src.constants import OPERATORS_ADD, OPERATORS_MUL, OPERATORS_POW, UNARY_OPERATORS
# Основная функция для вычисления значения выражения.
def parse_expression(tokens: list) -> float:

    now_token = 0
    result = add_function(tokens, now_token)
'''
    if tokens.count("(") != tokens.count(")"):
        return "Ошибка"

    copy_tokens = ''.join(tokens[::])
    brackets= [] # список, состоящий из кортежей - индексов открывающих скобок и соответствующих им закрывающих скобок
    while copy_tokens.find('(') != -1:
        brackets.append((copy_tokens.find('('), copy_tokens.rfind(')')))
        # Удаляем записанные скобки посредством замены на символ пробела, чтобы индексация не нарушилась
        copy_tokens = copy_tokens[:copy_tokens.find('(')] + ' ' + copy_tokens[copy_tokens.find('(')+1:copy_tokens.rfind(')')] + ' ' + copy_tokens[copy_tokens.rfind(')')+1:]
    brackets = brackets[::-1] # Переворачиваем, чтобы слева направо стояли скобки от внутренних к внешним

    tmp_list = [] # Создаем пустой массив, где буду храниться кортежи - (арифметическое значение выражения в скобках, \
    # индекс открывающей скобки, индекс закрывающей скобки
    for poz in brackets:
        now_token = 0
        tmp = add_function(tokens[poz[0]+1:poz[1]], now_token)
        tmp_list.append((tmp, poz[0], poz[1]))
    for res, poz1, poz2 in tmp_list:
        tokens = tokens[:poz1] + res + tokens[poz2+1:]
    now_token = 0
    return add_function(tokens, now_token)
'''
# Функция
def add_function(tokens: list, now_token: int) -> float:
    left_token = mul_function(tokens, now_token)
    while now_token < len(tokens):
        if tokens[now_token] in OPERATORS_ADD:
            operation = tokens[now_token]
            now_token += 1
            right_token = mul_function(tokens, now_token)
            left_token = add_operation(left_token, operation, right_token)
    return left_token

def mul_function(tokens: list, now_token: int) -> float:
    left_token = power_function(tokens, now_token)
    while now_token < len(tokens):
        if tokens[now_token] in OPERATORS_MUL:
            operator = tokens[now_token]
            now_token += 1
            right_token = power_function(tokens, now_token)
            if operator in '/%//' and right_token == 0.0:
                raise ZeroDivisionError("ДЕЛИТЬ НА НОЛЬ НЕЛЬЗЯ, БИТЮКОВ НАКАЖЕТ!!!")
            if operator in '//%':
                if ((str(right_token)[-2] + str(right_token)[-1]) in '.0') and (str(right_token)[-2] + str(right_token)[-1]) in '.0':
                    left_token = mul_operation_integer(left_token, operator, right_token)
                else:
                    raise ZeroDivisionError("НЕЛЬЗЯЯЯЯЯ")
            else:
                left_token = mul_operation_float(left_token, operator, right_token)

    return left_token


def power_function(tokens: list, now_token: int) -> float:
    left_token = unary_function(tokens, now_token)
    while now_token < len(tokens):
        if tokens[now_token] in OPERATORS_POW:
            now_token += 1
            right_token = power_function(tokens, now_token)
            left_token = left_token ** right_token
    return left_token


def unary_function(tokens: list, now_token: int) -> float:
    if tokens[now_token] in UNARY_OPERATORS:
        unary = tokens[now_token]
        now_token += 1
        digit = primary_function(tokens, now_token)
        if unary == '+':
            return digit
        elif unary == '-':
            return -digit

    return primary_function(tokens, now_token)


def primary_function(tokens: list, now_token_index: int) -> float:
    now_token = tokens[now_token_index]
    if now_token == '(':
        now_token_index += 1
        result = add_function(tokens, now_token_index)
        if (len(tokens) <= now_token) or tokens[now_token_index]  != ')':
            raise ValueError("СКОБКИ НЕ ЗАКРЫТЫ")
        now_token_index += 1
        return result
    else:
        now_token_index += 1
        try:
            return float(tokens[now_token_index])
        except ValueError:
            return 0.0


def mul_operation_float(left_token: float, operator, right_token: float) -> float:
    if operator in '*': return left_token * right_token
    else: return left_token / right_token

def mul_operation_integer(left_token: float, operator, right_token: float) -> float:
    if operator in '//': return left_token // right_token
    else: return left_token % right_token

def add_operation(left_token, operation, right_token) -> float:
    if operation in '+': return left_token + right_token
    else: return left_token - right_token

