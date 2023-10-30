nums=[34, 45,34,25,53,63,634,64,"rohit","choudhar"]
print(nums)
# listis mutable and allowed repeated value.
print(nums[3])
print(nums[-3])
print(nums[1:])
print(nums[-3:-1])

lis=["name",9.6,5,True]
print(lis)


nm=["lit",[34,34,353,534],[534],[34,434,433]]
print(nm[1][1:3])

print(nm.append(454545))
print(nm)
#nm.clear()
print("after the clear the nm list")
print(nm)
nm.insert(2,34505034)
nm.remove("lit")
x=nm.pop(4)
print(x)
nm.extend([4,454,64,64])
print(sum(nm))
