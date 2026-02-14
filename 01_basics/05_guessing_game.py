import random
num=random.randint(1,100)

guess=int(input("Guess number between 1 to 100 : "))

count=0

while(count!=5):
    if(guess==num):
        print("you won game in",count+1,"steps")
        break
    else:
        if(guess>num):
            guess=int(input("guess soemthing smaller : "))
        else:
            guess=int(input("guess something greater : "))
    count+=1
else:
    print("bad luck")

