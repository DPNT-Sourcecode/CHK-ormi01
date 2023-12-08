
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    if not validate(skus):
        return -1
    return 1

def validate(skus: str) -> bool:
    return True
