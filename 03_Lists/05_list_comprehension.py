# List comprehension
# advantages
# more time efficient and space efficent then loops
# require fewer lines of code
# Transforms iterative statement into a formula

# syntax :
# L=[expression for item in iterable if condition ==True]

# add 1 to 10 in list
L=[i for i in range(1,11)]
# print(L)

# scaler to vector multiplication
v=[5,6,7]
s=-3

c=[i*s for i in v]
# print(c)

# new list with squares of previous list
l=[1,2,3,4]
res=[i**2 for i in l ]
# print(res)

# print all numbers divisible by 7 in 1 to 100
res=[i for i in range(1,100) if i%7==0]
# print(res)

lang=['java','perl','js','c','python']

res=[i for i in lang if i[0]=='p']
# print(res)


# nested if with list comprehension
basket =['apple','guava','cherry','banana']
my_fruits=['apple','kiwi','banana']
# make a list of fruits that are in my_fruits and basket and starts with 'a'

res=[fruit for fruit in my_fruits if fruit in basket if fruit[0]=='a']
# print(res)

# nested list comprehension
# generate a 3*3 matrix
res=[ [i for i in range(0,3)] for j in range(0,3)]
# print(res)

# cartesian products using list comprehension
x=[1,2,3,4]
y=[5,6,7,8]

res= [j*i for j in x for i in y]

# print(res)