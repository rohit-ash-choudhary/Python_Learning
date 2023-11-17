def fact(n):
    fact_res=1;
    for i in range(2,n+1):
        fact_res=fact_res*i

    return fact_res


x=int(input("enter  the number : "))
y=fact(x)
print(y)
