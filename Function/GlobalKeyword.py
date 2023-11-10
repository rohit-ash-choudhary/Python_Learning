a=45 #global keyword
b=23
c=452
d=34
def Globa():
    #global a
    a=35
    x=globals()['c']
    x=43
    print(id(x))
    print(x)


Globa()
print(id(c))
print(c)