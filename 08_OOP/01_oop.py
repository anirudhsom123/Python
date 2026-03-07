# if a function is associated to a class then it is called method
# if a function exist independent to the class then it is called function
# L=[1,2,3,4]
# len(L) # function
# L.append(4) # method

class intro:
    # parametarized constructor
    def __init__(self,name,age):
        self.name=name 
        self.age=age
    
    # magic method
    def __str__(self):
        return 'hello my name is {} and i am {}'.format(self.name,self.age)

A=intro('anirudh',22)

print(A)


