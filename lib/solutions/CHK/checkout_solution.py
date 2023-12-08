
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    # list of products and their prices
    products = {"A": 50, "B": 30, "C": 20, "D": 15}

    # validate
    if not valid(skus, products):
        return -1

    # offers
    offers = {"A": {3: 130}, "B": {2: 45}}

    # iterate through string storing quantities
    basket = {}
    for sku in skus:
        if sku not in basket:
            basket[sku] = 1
        else:
            basket[sku] += 1

    # want to find the total_price
    total_price = 0
    for item in basket:
        if item not in basket:
            continue
        normal_price = products[item]
        basket_amount = basket[item]
        if (item in offers):
            (offer_quantity, offer_price) = [(k ,v) for k, v in offers[item].items()][0]
            total_price += (basket_amount // offer_quantity) * offer_price + (basket_amount % offer_quantity) * normal_price
        else:
            total_price += basket_amount * normal_price

    return total_price


def valid(skus: str, products: dict) -> bool:
    for sku in skus:
        if sku not in products:
            return False
    return True