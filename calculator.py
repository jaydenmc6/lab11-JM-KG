import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError(f"Cannot take square root of a negative number: {a}")
        return math.sqrt(a)
    except ValueError:
        raise


def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a


def logarithm(a, b):

    if a <= 0 or a == 1:
        raise ValueError(f"Invalid logarithm base: {a}. Base must be > 0 and != 1.")
    if b <= 0:
        raise ValueError(f"Invalid logarithm argument: {b}. Argument must be > 0.")
    return math.log(b, a)


def exp(a, b):
    return a ** b
