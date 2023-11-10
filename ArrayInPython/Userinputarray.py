from array import *

arr=array('i',[])

len=int(input("input the leng of aaray"))
print("enter the element of array")
for i in range(0,len):
    elem=int(input())
    arr.append(elem)


print(arr)
