# *args

def prodcut(*args):
    prodcut=1
    for p in args:
        prodcut*=p
    return prodcut

print(prodcut(1,2,3,4,5)) # args take multiple input as tuple 

# **kwargs

def country_capital(**kwargs):
    for (key,value) in kwargs.items():
        print(key,'->',value)

country_capital(india="delhi",nepal="kathmandu")