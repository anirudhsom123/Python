# length of string without using len()
count=0
s="hello world"
for i in s:
    count+=1
    
print(count)

# return user name from a string 
s="anirudh@gmail.com"
print(s.split('@')[0])

# count the frequency of char 'h' in string 'hello how r u hitesh'
s='hello how r u hitesh'
count=0
for i in s:
    if i=='h':
        count+=1       
print(count)

# program to remove a character from a string
s='hello how r u hitesh'
rem='h'
res=''
for i in s:
    if i==rem:
        continue
    else:
        res+=i
print(res)

# check if string is palindrome or not
s='madam'
i=0
e=len(s)-1
while(i<=e):
    if s[i]!=s[e]:
        print('not palindrome')
        break
    i+=1
    e-=1

if i>e:
    print('palindrome')


# write a program to count the number of words in a string


# write a python program to convert a string to title case with using title

# write a program that can convert an integer to a string




