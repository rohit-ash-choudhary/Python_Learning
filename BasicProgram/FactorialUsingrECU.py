def factrec(n):
    if n==1:
        return 1;
    else:
        return n * factrec(n-1)
test=factrec(5)

print(test)