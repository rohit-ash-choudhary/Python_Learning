f=open("multithreading.py",'r')
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())

f1=open("test.py",'w')

for i in f:
    f1.write(i)




print(f1.read())