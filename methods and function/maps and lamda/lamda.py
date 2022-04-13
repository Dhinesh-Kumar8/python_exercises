def square(num):
    return num**2
my_num=[1,2,3,4,5]
map(square,my_num)
    
print (list(map(square,my_num)))
def splicer(mystring):
    if len (mystring) % 2 == 0:
        return 'even'
    else:
        return mystring[0]
mynames =['john','cindy','sarah','kelly','mike']
print(list(map(splicer,mynames)))
def check_even(num):
    return num % 2 == 0
nums = [0,1,2,3,4,5,6,7,8,9,10]
print (filter(check_even,nums))