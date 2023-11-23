x=lambda a:a*2
print(x(5))

lis=[34,34,2,4,25,4,6,21,4,7,5,8,5,3,2,8,223,231,34]

x=list(map(lambda n:n%2==0,lis))

print(x)