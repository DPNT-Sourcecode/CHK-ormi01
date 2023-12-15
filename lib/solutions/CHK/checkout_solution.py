
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    # define prices and offers
    prices: dict = {"A": 50, "E": 40, "B": 30, "C": 20, "D": 15, "F": 10}
    offers: dict = {"A": [(5, 200), (3, 130)], "E": [(2, 0, "B")], "B": [(2, 45)], "F": [(3, 20)]}

    # initialise basket and the total price
    basket: dict = {sku: 0 for sku in prices}
    total_price: int = 0

    # count items in basket
    for sku in skus:
        if sku not in prices:
            return -1 # invalid input
        basket[sku] = 1 if sku not in basket else basket[sku] + 1

    # apply offers here
    for sku, amount in basket.items():
        if sku in offers:
            for offer in offers[sku]:
                if len(offer) == 3:  # special offer "buy x get y free"
                    offer_amount, _, free_sku = offer
                    basket["B"] = max(basket["B"] - (basket["E"] // 2), 0)
                else:  # regular offer "buy x for y price"
                    offer_amount, offer_price = offer
                    while amount >= offer_amount:
                        total_price += offer_price
                        amount -= offer_amount
        total_price += amount * prices[sku]

    return total_price



