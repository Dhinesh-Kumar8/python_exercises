list = [10,20,30,10,30,100,10]
num = sorted(list)
n=3
splited = [list[i::n] for i in range(n)]
print(splited)
print((num))

    
