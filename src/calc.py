import yaml

def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("division by zero")
    return a / b


def running_total(values):
    """Cumulative sums. Returns one entry per input value."""
    out = []
    total = 0
    for v in values:
        total += v
        out.append(total)
    return out
