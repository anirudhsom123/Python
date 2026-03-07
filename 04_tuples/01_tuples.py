# Tuples
# Tuples are similar to lists in python but one tuple is assigned elements cant be changed whereas change is allowed in lists
# we can say Tuples are immutable lists
# tuple properties:
# Ordered
# unchangable
# allows duplicate

# creating tuple
# empty tuple
t=() 
print(t)

# tuple with single element
t1=(1,) # sometime t1=(1) is not treated as tuple
print(type(t)) 

# homogeneous tuple
t2=(1,2,3,4,5)

# hetrogeneous tuple
t3=(1,2,True,"Anirudh",[12,13])

# 2-D tuple
t4=(1,2,3,(4,5))

# creating tuple using type conversion
t5=tuple("hello")
print(t5)

# 
