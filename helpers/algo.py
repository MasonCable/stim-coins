# Returns change in prices with neg and positive
def get_change(current, previous):
    
    if current == previous:
        return 0.0

    priceChange = (current - previous) / ((current + previous) / 2) * 100

    if current > previous:
        return priceChange
    else:
        return priceChange * -1