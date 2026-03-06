# list traversing

L=[10,20,30,40,50]
# itemwise traversing
# for i in L:
#     print(i)


# # indexwise traversing 
# for i in range(0,len(L)):
#     print(L[i])

# zip() function

# zip used to The zip() function in Python is like the zipper on a jacket. It takes two or more lists (or any sequences) and pairs their items together based on their position.
# The first item of the first list is paired with the first item of the second list, the second with the second, and so on.

L1=[1,2,3,4]
L2=[5,6,7,8]
ans=[i*j for i,j in zip(L1,L2)]
print(ans)