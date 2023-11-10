def count(lis):
    even=0
    odd=0
    for i in lis:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd



lis=[34,34,22,42,43,31,452,45,47,8,855,5,3]
even,odd= count(lis)
print(even)
print(odd)