def divi(a,b):
    if b>a:
        c=b
        b=a
        a=c
        return a/b
    else:
        return a/b

result=divi(2,5)
print(result)