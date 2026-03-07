def g(y):
    print(x) # will take value of x from global varibale 
    print(x+1)

x=10
g(5)
print(x)

def sum(y):
    global x # use global keyword if u want to modify the global keyword else modification is not allowed
    x+=1 # not allowed can't modify global varibale inside function

sum(x)
print(x)