# Lists Functions
 # len, min , max , sorted
 
L=[10,20,40,50]
print(len(L))

# min and max only works on homogeneous lists
print(min(L))
print(max(L))
print(sorted(L)) # ascending order sort
print(sorted(L,reverse=True)) # descending order sort

# count , index , reverse
L=[10,20,30,50,10,20,100]
print(L.count(10)) # will count the occurance of number provided returns 0 is element dont exist

print(L.index(10)) # will return 1st occurance of the element 

L.reverse() # will reverse list inplace
print(L)

# sort (vs sorted)
L.sort() # inplace sorting happens whereas sorted returns a sortes list
print(L)


# copy -> makes a shallow copy
L1=L.copy()
print(id(L))
print(id(L1))

# deepcopy
import copy
L2=copy.deepcopy(L1)
print(id(L2))

 