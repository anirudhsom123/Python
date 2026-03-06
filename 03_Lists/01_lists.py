# LIST VS ARRAY
# dynamic size (List) VS fixed size (Arrays)
# hetrogeneous (List) vs homogeneous (Arrays)
# speed of Execution arrays are fast then list
# Memory list occupy more space

# how are list stored in memory uses refrential array for storing addresses of corresponding data

L=[1,2,3]

# properties of list 
# ordered
# mutable
# hetrogeneous
# duplicates allowed
# are dynamic
# can be nested
# items can be accesied


# CREATING A LIST

# empty 
l=[]
# 1d list
l1=[1,2,3]
# 2d list
l2=[1,2,[3,4]]
# 3d list
l3=[1,2,[[3,4],5]]

# hetrogeneous
l4=[1,2,3.4,True,"anirudh"]

print(list('hello'))

# accessing items in list
l=[1,2,3,4,5]
print(l[0])
l=[1,2,[3,4]]
print(l[2][0])
# slicing in list

l=[1,2,3,4,5]
print(l[::-1])




