my_lst1=[1,2,3]
my_lst2=[4,5,6]
matrix =[my_lst1,my_lst2]
print(matrix)
print('\n')
new_stag = [item+1 for item in matrix[0]]
new_stag1 = [item+1 for item in matrix[1]]
print([new_stag,new_stag1])
print("logesh learned")
matrix_e=[[1,2,3],[4,5,6]]
matrix_2=[]
for arr in matrix_e:
    arr2 =[]
    for item in arr :
        arr2.append(item+1)
    matrix_2.append(arr2)
print(matrix_2)    
