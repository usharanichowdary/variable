#for loop:

l=[1,2,3,4,5]       
sum =0
for i in l:
    sum=sum+i
    print(sum)


# while loop:

c=0
while c<4:
    c+=1
    print("c is true")
else:
    print('completed loop')


#Break:

for val in 'chowdary':
    if val=='w':
        break
    print(val)
print('end')

#continue:

for val in 'usha':
    if val=='h':
        continue
    print(val)
print("end")

#pass

for val in 'rani':
    if val=='n':
        pass
    print(val)
print("end")

