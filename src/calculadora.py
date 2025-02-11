def soma(a, b):
    """Returns the sum of two numbers."""
    return a + b

def divide(a, b):
    """Returns the division of a by b, handling division by zero."""
    if b == 0:
        raise ValueError("Não é possivel dividir por zero")
    return a / b

