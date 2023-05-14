lst=[x for x in 'word']
print(lst)
#example2
lst=[x**2 for x in range(0,11)]
print(lst)
#example3
lst=[x for x in range(11) if x%2==0]
print(lst)
#example4
celsis=[0,10,20.1,34.5]
fahrenheit =[((9/5)*temp +32) for temp in celsis]
print(fahrenheit)
#example5
lst=[x**2 for x in [x**2 for x in range(11)]]
print(lst)