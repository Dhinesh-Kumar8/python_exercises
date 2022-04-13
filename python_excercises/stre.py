stock_prices = [('AAPL',700),('GOOG',350),("MSFT",400)]
def min_prices(stock_prices):
    min =10000000
    stock=None
    for stock,prices in stock_prices:
        if prices < min :
            min = prices
        else:
            pass 
    return min
am = min_prices(stock_prices)
print(am)