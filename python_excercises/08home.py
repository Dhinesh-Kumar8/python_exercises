from typing import Counter


pogo = [3,1,2,4,5]
cartoon = [2,3,4,1,5,9]
#output:true
x = sorted(pogo)
y = sorted(cartoon)
d = zip(x,y)
m = []
same=True
for num,num2 in d:
  if num!=num2:
        same = False
print(same) 


a =[True,True,False,True]
b=True
for num in a:
  if num==False:
        b=False
print(b)
    


      