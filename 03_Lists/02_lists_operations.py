l=[1,2,3,4]
# adding items to list
# append
l.append(True)
# extend
l.extend([6,7,8])
l.extend('delhi')

# insert adding at desired index
l.insert(1,100)
print(l)


# Editing on List

# edting via index
L=[10,20,30,40]
L[0]=11
# editing via slicing
L[1:]=[21,31,41]
print(L)

# Deleting list
# dl
del L
# print(L) # Error  L is not defined
L=[1,2,3,4,5,6,7]
del L[0]
print(L)
del L[0:3]
print(L)


# remove deleting value via entering value instead of index
L=[10,20,30,40,50]
L.remove(30)

print(L)

# pop used to delete via index or if index not provided removes the last element 
L=[10,20,30,40,50]
L.pop(0) # remove 10 from list
L.pop() # remove 50 from list

# clear - remove all items from the list 
L=[10,20,30,40,50]
L.clear()

print(L)

