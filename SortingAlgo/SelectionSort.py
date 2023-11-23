def SelectionSort(list):
    for i in range(len(list)-1):
        imin=i
        for j in range(i,len(list)):
            if list[j]<list[imin]:
                imin=j
        temp=list[i]
        list[i]=list[imin]
        list[imin]=temp
        return list

list=[34,23,5,5,34,23,57,46,75,34,2,7,373,597,79,43,89]
res=SelectionSort(list)
print(res)
