
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    # list of products and their prices
    products = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}

    # validate
    if not valid(skus, products):
        return -1

    # offers
    offers = {"A": {3: 130, 5: 200}, "B": {2: 45}, "E": {2: 30}}

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
        normal_price = products[item]
        basket_amount = basket[item]
        total_price += basket_amount * normal_price

    # apply offers
    for item in basket:
        if item not in offers:
            continue
        biggest_saving = 0
        normal_price = products[item]
        for (offer_quantity, offer_price) in offers[item].items():
            saving = (basket_amount * normal_price) - (basket_amount // offer_quantity) * offer_price
            if saving > biggest_saving:
                biggest_saving = saving
        total_price -= biggest_saving

    return total_price


def valid(skus: str, products: dict) -> bool:
    for sku in skus:
        if sku not in products:
            return False
    return True