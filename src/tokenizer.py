import re

def tokenizer(expression: str) -> list:
    token_re = re.compile(r"""
        \s*
        (
            \d+(?:\.\d+)?         # число
          | \*\*                   # ** (обязательно раньше *)
          | //                       # //
          | [%()+\-*/]              # одиночные токены
        )
    """, re.VERBOSE)
    tokens = [m.group(1) for m in token_re.finditer(expression)]
    return tokens
