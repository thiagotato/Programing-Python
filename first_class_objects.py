import operator

OPERATOR_MAPPING = {
        '+': operator.add,
        '-': operator.sub,
        '/': operator.truediv
        }

def perform_operation(op, lhs, rhs):
    if op == '+':
        return lhs + rhs
    if op == '-':
        return lhs - rhs
    if op == '/':
        return lhs / rhs

def calc(op, lhs, rhs):
    return OPERATOR_MAPPING[op](lhs, rhs)
