#range
from random import randint, shuffle
print("int1")
print(range(0,11))
print("int2")
print(list(range(0,11)))
print("int3")
print(list(range(0,12)))
print('int4')
print(list(range(0,11,2)))
print("int5")
print(list(range(0,101,10)))
#enumerate
index_count=0
for letter in'abcde':
    print("at index {} the letter is {}".format(index_count,letter))
    index_count+=1
print(list(enumerate('abcde')))
print("#zip")
mylist1=[1,2,3,4,5]
mylist2=["a","b","c","d","e"]
print(list(zip(mylist1,mylist2)))
for item1,item2 in zip(mylist1,mylist2):
    print("for this tuple,first item was {} and second item was {}".format(item1,item2))
print("IN OPERATOR")
print("x" in ["x","y","z"])
print("x"in [1,2,3])
print("x"not in["x","y","z"])
print("x" not in [1,2,3])
print("MIN AND MAX")
mylist=[10,20,30,40,100]
print(min(mylist))
print(max(mylist))
shuffle(mylist)
print(mylist)
print("\n")
print(randint(0,100))
print(randint(0,100))
#input
input("enter something in this box: ")