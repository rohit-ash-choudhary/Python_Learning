#Data Types

"""
1. None
2. Numeric : Int , float , complex , Bool
3. Series : List, Tuple, Set , Dictionary




"""
a=None #None
b=34  #int
c=43.2 #float
d=4+5j #conplex
e=True #Boolean

z=complex(b,c) #Complex
print(z)


lis=["abc",34,65.4 ,34+8j, True]
lis.append(34)
print(lis) # mutable and ordered

Tupe =(34, 534, 534,645,6456,454) # immutable and ordered
print(Tupe)

set={34,34,34,34,3534,6456,54645,7567,34,565,7576,57657656,7657}
print(set)

dict1={"name": "megha", "lastname": "joshi","phonenumner":7611988883}
print(dict1["name"])
print(dict1)
print(dict1.keys())
print(dict1.values())
aa=list(range(10))
print(aa)


