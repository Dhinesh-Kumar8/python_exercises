num1 = input("enter  first number")
num2 = input("enter second number")
sum = float(num1)+float(num2)
print('the sum of {0} and {1} is {2}'.format(num1,num2,sum))
#nextprogram
def maximum(a,b):
    if a>=b:
        return a
    else:
        return b
a = 2
b = 4
print(maximum(a,b))