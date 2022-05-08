from tokenize import Number

google = [10,20,30,10,30,100,100]


def duplicate_finder(google):
    Number = google
    duke = []
    for num in sorted(list(set(Number))) :
        mylist = []
        for num2 in Number:
            if num == num2:
                mylist.append(num)
        duke.append(mylist)
    return duke


print(duplicate_finder(google)) 

    
                
                
                
            