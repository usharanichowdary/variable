
#number patterns
n=5
p=1
for i in range(n):
    for j in range(i+1):
        print(p,end=' ')
    p+=1
    print()

n=5
for i in range(n):
    for j in range(i+1):
        if(i%2==0):
            print(1,end=' ')
        else:
            print(2,end=' ')
    print()

#factors

num=8
for i in range(1,num+1):
    if (num%i==0):
        print(i)

#prime number

num=11
count=0
for i in range(1,num+1):
    if(num%i==0):
        count+=1
    if(count==2):
        print("prime number")
    else:
        print("not prime number")
