
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    # define prices and offers
    prices: dict = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10}
    offers: dict = {"A": [(5, 200), (3, 130)], "B": [(2, 45)]}

    # initialise basket and the total price
    basket: dict = {}
    total_price: int = 0

    # count items in basket
    for sku in skus:
        if sku not in prices:
            return -1 # invalid input
        basket[sku] = 1 if sku not in basket else basket[sku] + 1

    # add 2E->1B offer before any other offer on B is applied
    # can be proven by induction that 2E->1B > 2B->45
    if "B" in basket and "E" in basket:
        basket["B"] = max(basket["B"] - (basket["E"] // 2), 0)

    # work on the F offer here
    if "F" in basket:
        if basket["F"] >= 3:
            basket["F"] = (basket["F"] // 3) * 2 + (basket["F"] % 3)

    # apply offers here
    for sku, amount in basket.items():
        if sku in offers:
            for offer_amount, offer_price in offers[sku]:
                while amount >= offer_amount:
                    total_price += offer_price
                    amount -= offer_amount
        total_price += amount * prices[sku]

    return total_price


