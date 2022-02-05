my_lst1=[1,2,3]
my_lst2=[4,5,6]
matrix =[my_lst1,my_lst2]
print(matrix)
print('\n')
new_stag = [item+1 for item in matrix[0]]
new_stag1 = [item+1 for item in matrix[1]]
print([new_stag,new_stag1])
