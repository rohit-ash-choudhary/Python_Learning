def variarug(a,*b):
    c=a
    for i in b:
        c+=i
    return c

lt=variarug(4,3,5,2,5,34,232)
print(lt)