a=2
b=23
if a>b:
   print('false')
elif a<b:
   print('true')
else:
   print('true')



x=20
if x>25:
    print("if cond is true")
elif x<25:
    print("cond is true")
else:
    print("if cond is false")




#By nested loop
x = 10
y = 20

if x > 5:
    print("x is greater than 5")
    if y > 15:
        print("y is also greater than 15")
    else:
        print("y is not greater than 15")
else:
    print("x is not greater than 5")


#By using logical operators

x=10
y=20
z=30

if x>5:
    if y>15 and z>25:
        print('x is greater than 5,y is greater than 15,z is greater than 25')
    elif y<15 and z<=25:
        print('x is greater than 5,y is lesser than 15,z is lessere than or equal to 25')
    else:
        print('x is greater than 5, y is lesser than 15')
else:
    print('x is lesser than 5')
