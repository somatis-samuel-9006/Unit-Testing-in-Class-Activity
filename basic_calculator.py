def addition(x, y):
    if(isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return x + y
    else:
        return "Invalid input"

def subtraction(x, y):
    try:
        return x - y
    except TypeError:
        return "Invalid input"

def multiplication(x, y):
    if(isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return x * y
    else:
        return "Invalid input"

def division(x, y):
    try:
        return x / y
    except (ZeroDivisionError, TypeError):
        return "Invalid input"
        