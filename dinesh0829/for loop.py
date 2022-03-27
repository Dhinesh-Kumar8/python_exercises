beast=[1,2,3,4,5,6,7,8,9,10]
for num in beast:
    print(num)
print("example2")
for num in beast:
    if num %3==0:
        print(num)
    else:
        print("odd number")
print("example3")
list_sum=0
for num in beast:
    list_sum=list_sum+num
    print(list_sum)
list_sum=0
print("--------------")
for num in beast:
    list_sum+=num
    print(list_sum)
print("example4")
for letter in "this is a string.":
    print(letter)
print("example5")
tup=(1,2,3,4,5)
for t in tup:
    print(t)
print('example6')
list2=[(2,4),(6,8),(10,12)]
for tup in list2:
    print(tup)
print("-------------")
for (t1,t2)in list2:
    print(t1)
print("example7")
d={"k1":1,"k2":2,"k3":3}
for item in d:
    print(item)
#creating a dictionary
print(d.items())

for k,v in d.items():
    print(k)
    print(v)
print("key is used")
print(list(d.keys()))
print(sorted(d.values()))