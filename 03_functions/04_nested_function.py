# nested functions
def f():
    def g():
        print('functions g is printed')
    g()
    print("finction f is printed")

f()
# g() # can't call inner function
