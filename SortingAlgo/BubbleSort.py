def BubbleSort(lis):
    flag=0;
    for i in range(0,len(lis)):
        for j in range(0,len(lis)-1):
            if lis[j]>lis[j+1]:
                new=lis[j]
                lis[j]=lis[j+1]
                lis[j+1]=new
    return lis

lis=[34,23,5,5,34,23,57,46,75,34,2,7,373,597,79,43,89]

res=BubbleSort(lis)
print(res)


