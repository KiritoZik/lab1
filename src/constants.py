import operator

OPERATORS_ADD = {
    "+": operator.add,
    "-": operator.sub
}

OPERATORS_MUL={
    "*": operator.mul,
    "/": operator.truediv,
    "//": operator.floordiv,
    "%": operator.mod
}

OPERATORS_POW = {
    "**": operator.pow,
}

UNARY_OPERATORS = ["+", "-"]

ALL_OPERATORS = ['*', '/', '//', '%', '**', '+', '-']

ERROR_COMBINATION = ['%+', '%-', '%/', '%*', '%//', '%**', '+%', '+-', '+/',
                     '+*', '+//', '+**','-%', '-+', '-/', '-*', '-//', '-**', '/%', '/+', '/-', '/*', '///',
                     '/**', '*%', '*+', '*-', '*/', '*//', '***', '//%', '//+', '//-', '///', '//*', '//**',
                     '**%', '**+', '**-', '**/', '***', '**//', '++', '--', '////', '%%', '****']
