# sum of digits of a number

num=int(input('Enter the number : '))

ans=0

while(num!=0):
    rem=num%10
    num=num//10
    ans+=rem

print(ans)