from array import *


arr=array('I',[343,34,53,54,64,33]);
print(arr.buffer_info())
arr.reverse()
print(arr)

for i in arr:
    print(i)


for i in range(len(arr)):
    print(i)




squew_arr=array(arr.typecode,(i**2 for i in arr))
print(squew_arr)