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
