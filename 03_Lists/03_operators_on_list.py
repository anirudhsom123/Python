# arithmetic operators only (+ and *) are allowed on lists
L1=[10,20,30]
L2=[40,50,[20,30]]

print(L1+L2) # merge two list

print(L1*3)

# membership operators
print(20 in L1)
print([20,30] in L2)

# Loops 
for i in L1:
    print(i)

for i in L2:
    print(i)

