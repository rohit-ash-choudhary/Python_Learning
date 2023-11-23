def seach(lit,n):
    for i in range(0,len(lit)):
        if lit[i]==n:
            return i
    else:
        return "intem not found in list"

re=seach([34,2,4,2,7,5,889,5,342,1,3,0,9],2)
print(re)


print("hello: manoj: lodu ")