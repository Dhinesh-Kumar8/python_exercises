list1 = [101,2,3,6,8]
list2 = [6,8,9,3,2,101]
#output = [6,8,3,2]
def list_compare(list1,list2):
    mylist =[]
    for num in list1:
        for num2 in list2:
            if num==num2:
                mylist.append(num)
    print(mylist)
    return mylist
print(list_compare(list1,list2))      
    