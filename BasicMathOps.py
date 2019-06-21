def basic_op(operator, value1, value2):
    if operator == 'Addition':
        return value1 + value2
    elif operator == 'Subtraction':
        return value1 - value2
    elif operator == 'Multiplication':
        return value1 * value2
    elif operator == 'Division':
        return value1 / value2
    else:
        return "Unrecognized Operator. Please select from Addition, Subtraction, Multiplication or Division"
