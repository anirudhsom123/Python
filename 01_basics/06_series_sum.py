# sum of series = 1/1! + 2/2! + 3/3! . . . . . + n/n!

n=int(input("enter the number : "))

def factorial(num):
    fact=1
    for i in range(num,0,-1):
        fact*=num
        num-=1
    return fact 

ans=0
for i in range(1,n+1):
    ans+=i/factorial(i)

print(ans)

