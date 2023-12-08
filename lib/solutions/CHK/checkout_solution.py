
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    # validate
    if not validate(skus):
        return -1
    
    # dictionary of prices containing offers too
    price = {}
    price["A"]["offer"][3] = 130 
    price["A"]["price"] = 50
    price["B"]["offer"][2] = 45
    price["B"]["price"] = 30
    price["C"]["price"] = 20
    price["D"]["price"] = 15

    # create a dictionary to represent basket
    basket = {}
    for item in skus:
        if item in basket:
            basket[item] = 0
        else:
            basket[item] += 1

    # now want to apply offers
    for item in basket:
        # see if there is enough offers 



def validate(skus: str) -> bool:
    return True