# Returns change in prices with neg and positive
def get_change(currentPrice, buyPrice):
    if currentPrice == buyPrice:
        return 0.0

    priceChange = (currentPrice - buyPrice) / ((currentPrice + buyPrice) / 2) * 100

    if buyPrice < currentPrice:
        return priceChange * -1
    else:
        return priceChange