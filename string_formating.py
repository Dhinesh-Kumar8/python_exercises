


print("i'm going to inject %s here."%'something')
print('\n')
print ("i'm going to inject %s text here,and %s text here."%('some','more'))

x,y='some','more'
print("i'm going to inject %s better text,and %s most text."%(x,y))
print('\n')
print("he said his name was %s."%'dhinesh kumar')
print('he said his name was %r.'%"dhinesh kumar")
print('\n')
print("once upon caught fish %s."%'this \tbig')
print('once upon time king %r.'%"this \thorour")
print("\n")
print('i wrote %s program a day.'%3.75)
print("i wrote %d program a day."%3)
print("\n")
print('the floating point number:%5.2f'%(13.144))
print("the floating point number:%1.0f"%(13.144))
print('the floating point number:%1.5f'%(13.144))
print("the floating point number:%10.2f"%(13.144))
print("the floating point number:%25.2f"%(13.144))
print("\n")
print('first:%s,second:%5.2f,third:%r.'%('hi!',3.1415,"bye!"))
print("the is a string with an {}".format('insert'))
print("the {2} {1} {0}".format("fox","brown","quick"))
print("\n")
print("first object:{a},second object:{b},third object:{c}".format(a=1,b="two",c=12.3))
print("\n")
print("a %s saved is a %s earned."%("penny","penny"))
print("a {p} saved is a {p} earned".format(p="penny"))
print("\n")
print('{0:8} ! {1:9}'.format("fruit","quantity"))
print("{0:8} ! {1:9}".format("apple",3.))
print("{0:8} ! {1:9}".format("orange",10))
print("\n")
print("{0:<8} ! {1:^8} ! {2:>8}".format("left","center","right"))
print("{0:<8} ! {1:^8} ! {2:>8}".format(11,22,33))
print("\n")
print("{0:=<8} ! {1:-^8} !{2:.>8}".format("left","center","right"))
print("{0:=<8} ! {1:-^8} !{2:.>8}".format(11,22,33))
print("\n")
name="SURYA"
print(f"he said his name is {name}")
print("\n")
num=23.45
print("my 10 character,four decimal number is:{0:10.4f}".format(num))
print(f"my 10 character,four decimal number is:{num:{10}.{6}}")
num=23.54
print("my 10 character,four decimal number is:{0:10.4f}".format(num))
print(f"my 10 character,four decimal number is:{num:10.4f}")