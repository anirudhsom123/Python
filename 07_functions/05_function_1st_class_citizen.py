# funtions in python are 1st class citizen

def square(a):
    return a**2

# type and id
type(square) # type of square i.e. function
id(square) # address of function


# reassign function
a=square # assigned square to a 

print(a(3))
# deltecing function

del square # square will be deleted

# storing function in list
def square(a):
    return a**2

L=[1,2,3,5,square]
print(L[-1](3))

# returning function
def f():
    def x(a,b):
        return a+b
    return x

x_fun=f()
print(x_fun(2,3))

# function as argument

def func_a():
    print("inside function a")

def func_b(z):
    print("inside function b")
    return z()

func_b(func_a)

