from operator import index
from re import I

arr = [10,20,30,10,30,100,10]
new_arr = []
for i in arr:
    val_arr = []
    for j in arr:
        if i == j:
            val_arr.append(i)
    new_arr.append(val_arr)    
            
print(new_arr)
