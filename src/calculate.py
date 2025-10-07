from src.tokenizer import tokenizer
from src.parser import parse_expression

def calculate(expression: str) -> float:
    tokens = tokenizer(expression)
    return parse_expression(tokens)
