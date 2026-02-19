# reduce is not inbuilt function
# it is part of functools module

import functools

# sum of elements in an array
print(functools.reduce(lambda x,y:x+y , [1,2,3,4,5]))

# min element from an array
print(functools.reduce(lambda x,y:x if x<y else y,[12,3,4,7,18]))

