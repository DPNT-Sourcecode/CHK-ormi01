
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    # define prices and offers
    prices: dict = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10, "G": 20, "H": 10, 
                    "I": 35, "J": 60, "K": 80, "L": 90, "M": 15, "N": 40, "O": 10, "P": 50, 
                    "Q": 30, "R": 50, "S": 30, "T": 20, "U": 40, "V": 50, "W": 20, "X": 90, 
                    "Y": 10, "Z": 50}
    offers: dict = {"A": [(5, 200), (3, 130)], "E": [(2, 0, "B")], "B": [(2, 45)], "F": [(3, 20)], "H": [(10, 80), (5, 45)],
                     "K": [(2, 150)], "N": [(3, 0, "M")], "P": [(5, 200)], "Q": [(3, 80)], "R": [(3, 0, "Q")], "U": [(4, 120)], 
                     "V": [(3, 130), (2, 90)]}

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

