
a = [2,1,3,4,5,7]
b = [1,2,4,5,6,7]
#output = [2,2,4,5,6]
moon=[]
x = zip(a,b)
for num,num2 in x:
        if num<num2:
            moon.append(num2)
        elif num2<num :
            moon.append(num)
        else:
            moon.append(num2)
print(moon)
        
        
            
        
        