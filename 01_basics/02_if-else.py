# conditionals

mail="ani@gmail.com"
password=12345

if(mail=="ani@gmail.com" and password==12345):
    print("valid user")
elif(mail=="ani@gmail.com" and password!=1234):
    print("one entry is wrong")
else:
    print("invalid user")

# nested if else


# max of 3 numbers
a=20
b=50
c=14
if(a>b):
    if(a>c):
        print(a)
    else:
        print(c)
elif(b>a):
    if(b>c):
        print(b)
    else:
        print(c)

#basic calculator
num1=int(input("enter number 1 : "))
num2=int(input("enter number 2 : "))
opr=input("Enter operator + , - , // , * : ")

if(opr == "+"):
    print(num1+num2)
elif(opr == "-"):
    print(num1-num2)
elif(opr == "*"):
    print(num1*num2)
elif(opr == "//"):
    print(num1//num2)
else:
    print("enter valid operator or valid numbers")