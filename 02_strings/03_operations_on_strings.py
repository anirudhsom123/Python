# some arhtematic operators and relational operators works on Strings
# Arthematic Operations
# + and * operators are allowed on strings
print('delhi'+' '+'mumbai')  # + operator used for concatination
print('*'*50) # no specific use can be utilized if needed

# Relational Operations
print('delhi'=='delhi') # true
print('delhi'!='mumbai') # true
print('delhi'=='mumbai') # false
print('delhi'>'mumbai') # false since ascii value of 'm' is greater then 'd'
print('delhi'<'mumbai') # true since ascii value of 'm' is greater then 'd'
print('delhi'>='delhiy',"*********") # true since ascii value of delhi is less then equal to mumba
# Logical Operations
# empty string false
# string with some value is true

print('' and 'hello') # true and false  answer will be false empty string 
print('hello' and 'world') # true and true will resturn last value i.e world
print('' or 'hello') # false or true returns true i.e hello
print('hello' or 'world') # true or true returns 
print(not 'hello') # not true returns false


# loops on Strings
for i in 'hello':
    print(i)
    
for i in 'delhi':
    print('pune')
    

# membership Operators
print('D' in "Delhi") # true since D is present in delhi
print('s' not in "delhi") # true since s in not in delhi


