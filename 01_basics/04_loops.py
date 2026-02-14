num=int(input("Enter the number : "))

# while loop
i=1

while(i<=10):
    print(i*num)
    i+=1

# while with else

k=0
while k<3:
    print(k)
    k+=1
else:
    print("while loop ended")


# for loop 
for j in range(1,11):
    print(num,"*",j,"=",j*num)