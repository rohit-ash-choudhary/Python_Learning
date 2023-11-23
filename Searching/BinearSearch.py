def Binsearch(list, n):
    int_i=0;
    lst_i=len(list)-1
    while(lst_i>int_i):
        mid=int((int_i+lst_i)/2)
        if list[mid]==n:
            return mid
        elif(list[mid]>n):
            int_i=mid
        else:
            lst_i=mid

res=Binsearch([10,21,32,43,45,67,78,90,100,103,105,110,115],78)
print(res)


