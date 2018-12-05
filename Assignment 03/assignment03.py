def check_error(expression):
    # check for ;
    operators = '+-*/'
    if expression[-1] != ';':
        return True
    if expression.count('(') != expression.count(')'):
        return True
    for i, cha in enumerate(expression):
        if cha in operators:
            if i == len(expression) - 1:
                return True
            value = expression[i+1]
            if not value.isdigit() or value != '(':
                return True
            break
    return False

