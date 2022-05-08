from tokenize import Number
list = [10,20,30,10,30,100,10]
Number = sorted(list)
print((Number))
for num in Number :
    first_Number = num
    for index in Number:
        second_number = index
        if num == index:
            print(Number)
        else:
            print([])
        