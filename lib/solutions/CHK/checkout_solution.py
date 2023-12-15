
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    # define prices and offers
    prices: dict = {"A": 50, "E": 40, "B": 30, "C": 20, "D": 15, "F": 10}
    offers: dict = {"A": [(5, 200), (3, 130)], "E": [(2, 0, "B")], "B": [(2, 45)], "F": [(3, 20)]}

    # initialise basket and the total price
    basket: dict = initialise_basket(prices, offers)
    total_price: int = 0

    # count items in basket
    for sku in skus:
        if sku not in prices:
            return -1 # invalid input
        basket[sku] += 1

    # apply offers here
    for sku, amount in basket.items():
        if sku in offers:
            for offer in offers[sku]:
                if len(offer) == 3:  # special offer "buy x get y free"
                    offer_amount, _, free_sku = offer
                    basket[free_sku] = max(basket[free_sku] - (basket[sku] // offer_amount), 0)
                else:  # regular offer "buy x for y price"
                    offer_amount, offer_price = offer
                    while amount >= offer_amount:
                        total_price += offer_price
                        amount -= offer_amount
        total_price += amount * prices[sku]

    return total_price

def initialise_basket(prices: dict, offers: dict):
    basket: dict = {sku: 0 for sku in prices}

    # sort basket
    sorted_keys = sorted(basket, key=lambda sku: (not any(len(offer) == 3 for offer in offers.get(sku, [])), sku not in offers))

    # create a sorted dictionary
    sorted_basket = {sku: basket[sku] for sku in sorted_keys}

    return sorted_basket





