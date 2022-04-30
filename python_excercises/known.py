arr = [10,20,30,10,30,100,10]
num = sorted(arr)
n=3
splited = [arr[i::n] for i in range(n)]
print(splited)
print((num))
stock_prices=[('AAPL',200),('GOOG',300),("MSFT",400)]