# lambda function is a small anonymous function
# lambda function can have any nnumber of arguments but can only contain one expression
# diff in lambda and normal function
# 1 No name for lambda functions
# 2 lambda function have no return value(infact returns a function)
# 3 lambda is written in oneline
# 4 not reusable
# where is lambda functions used , ans = used in Higher Order Function


# eg. x->x^2
a = lambda x:x**2
print(a(2))

# eg. x,y -> x+y
b= lambda x,y:x+y
print(b(10,20))

# eg. check if string contains a
c= lambda s:'a' in s
print(c('hello'))

# eg. number is odd or even
# d=lambda num:'even' if num%2==0 else 'odd'
d = lambda num:num%2==0
print(d(13))

