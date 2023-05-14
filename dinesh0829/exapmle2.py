Strings=["1","2","3","4","5"]
new_strings=[]
for string in Strings:
    new_string =string.replace("1","star")#modify old string
    new_strings.append(new_string)
    print(new_strings)
    print("\n")
my_str = [1,2,3]
print(my_str)
my_str.reverse()
print(my_str)
print("\n")
#logesh anna learned
arr =[1,2,3,4,5,6]
arr2=[]
repl_str = "hibye"
for item in arr:
    if item == 1:
        arr2.append(repl_str)
    else:
        arr2.append(item)

print(arr2)
