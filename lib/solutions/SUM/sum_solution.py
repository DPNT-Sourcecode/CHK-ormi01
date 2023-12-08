# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x: int, y: int) -> int:
    if valid(x, y):
        return x + y
    else:
        raise ValueError("Arguments provided must be between 0 and 100")

def valid(x: int, y: int) -> bool:
    return (x >= 0 and x <= 100) and (y >= 0 and y <= 100)