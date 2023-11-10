def add(a,b,c):
    return a+b+c;

l=add(3,5,3)
print(l)

def detail(name, age):
    print(name)
    print(age+5)

det=detail("Rohitash",23)
dett=detail(age=23,name="rohtisah")
print(det)
print(dett)




def detaill(name, age=18):
    print(name)
    print(age+5)
cult=detaill("rohitash")
print(cult)