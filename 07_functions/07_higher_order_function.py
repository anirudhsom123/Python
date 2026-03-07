# high order function
# what are high orde function ?
# 1. function that recive funtion as input in function

# eg. square of all numbers in a list

def square(a):
    return a**2
# higher order function
def transform(square,L):
    output=[]
    for i in L:
        output.append(square(i))
    print(output)


L=[1,2,3,5]
# transform(square,L)
transform(lambda x:x**2,L)



