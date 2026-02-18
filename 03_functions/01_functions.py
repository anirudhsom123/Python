# rule order of parameters in functions matter (vairables->*args->**kwags)
# args and kwargs are just for convenience not rule or manditory
# functions
#functions with docstring
def is_even(a):
    '''
    Docstring for is_even
    
    :param a: Description
    '''
    if(type(a)==int):
        return a%2==0
    return "Enter the valid number"


print(is_even.__doc__) # accessing docstring of any function
print(is_even(2)) # valid input
print(is_even(5)) # valid input
print(is_even("ani")) # invalid input