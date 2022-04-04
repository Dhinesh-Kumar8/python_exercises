from operator import truediv
from pickle import APPEND
from unittest import result


def say_hello():
    print('hello')
print(say_hello())
#accept parameter
def greeting(name):
    print(f'hello {name} ')
greeting('jose')
#return function
def add_num(num1,num2):
    return num1+num2
print(add_num(4,5))
print(add_num(100,50))
result =add_num(4,5)
print(result)
result= add_num(100,50)
print(result)
print(add_num("one","two"))
def print_result(a,b):
    print(a+b)
def return_result(a,b):
    return a+b
print_result(10,5)
#it cannot come output in.py script
return_result(10,5)
my_result = print_result(20,20)
print(type(my_result))
my_result = return_result(20,20)
print (my_result)
print(my_result+my_result)
#recall of module operator 
print(2%2)
print(20%2)
print(21%2)
print(20 % 2 ==0)
print(21 % 2 ==0)
# logical operation
def even_check(number):
    return number % 2 ==0  
print(even_check(20))
print(even_check(21))
def check_even_list(num_list):
    for number in num_list:
        if number % 2==0:
            return True
        else:
            pass
print(check_even_list([1,2,3]))
print(check_even_list([1,1,1]))
#logiacl common error
def check_even_list(num_list):
    for number in num_list:
        if number % 2==0:
            return True
        else:
            return False
print(check_even_list([1,2,3]))
def check_even_list(num_list):
    for number in num_list:
        if number % 2==0:
            return True
        else:
            pass
    return False
print("output1")
print(check_even_list([1,2,3]))
print("output2")
print(check_even_list([1,3,5]))
#return all even number in list
def check_even_list(num_list):
    even_numbers=[]
    for number in num_list:
        if number% 2==0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers
print(check_even_list([1,2,3,4,5,6]))
print(check_even_list([1,3,5]))
stock_prices=[('AAPL',200),('GOOG',300),("MSFT",400)]
for item in stock_prices:
    print(item)
for stock,price in stock_prices:
    print(stock)
for stock,price in stock_prices:
    print(price)
    