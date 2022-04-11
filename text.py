def add_num(num1,num2):
    return num1+num2
print(add_num(4,5))
def sub_num(num3,num4):
    return num3-num4
print(sub_num(5,6))
result=add_num(4,5)+sub_num(5,6)
print(result)
stock_prices=[('AAPL',200),('GOOG',300),("MSFT",400)]
for k,v in stock_prices.item():
        print(k)
        print(v)
        print(max(v))