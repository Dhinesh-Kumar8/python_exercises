list1=[1,2,3,4,5,6,7,8,9,10]
for num in list1 :
    print(num)
    #module denoted as %
print("\n")
print(17%5)
#module for remainder 
print(10%3)
print(18%7)
print(4%2)
print("EXAMPLE")
for num in list1:
    if num % 2 == 0:
        print(num)
print("using else")
for num in list1:
    if num % 2 == 0:
        print(num)
    else:
        print("odd number")
print("example 3")
# Start sum at zero
list_sum = 0 
for num in list1:
    list_sum = list_sum + num
    print(list_sum)
print("nxt")
list_sum = 0
for num in list1:
    list_sum += num
    print(list_sum)
print("example 4")
for letter in 'this is string .':
    print(letter)
print("example 5")
tup=(1,2,3,4,5)
for t in tup:
    print(t)
print("example 6")  
list2 = [(2,4),(6,8),(10,12)]
for tup in list2:
    print(tup)
for (t1,t2) in list2:
    print(t1)
print("example 7")
dinesh ={"k1":1,"k2":2,"k3":3}
for item in dinesh:
    print(item)
# Create a dictionary view object
print(dinesh.items())
#dictionary unpacking
for k,v in dinesh.items():
    print(k)
    print(v)
print(list(dinesh.keys()))
print(sorted(dinesh.values()))