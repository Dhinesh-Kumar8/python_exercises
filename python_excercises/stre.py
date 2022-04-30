stock_prices1 = [('AAPL',700),('GOOG',3050),("MSFT",400)]
def min_prices(stock_prices):
    min =10000000
    stock=None
    for stock,prices in stock_prices:
        if prices < min :
            min = prices
        else:
            pass 
    return min
am = min_prices(stock_prices1)
print(am)


arr = [10,20,30,10,30,100,10]

out = [(10,10,10),20,(30,30),100]