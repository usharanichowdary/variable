# functions using parameters

def add(a,b):
    return(a+b)
print(add(2,5))

def wish():
    print('hello world')
    return
print(wish(),wish())


#orbitary arg

def fun(*a):
    print("this is a function",a)
fun(1,2,3)

#kwargs
# 1)
def usha(**a):
    print(a)
usha(name="chinni",age=24)

# 2)

def details(name,age,mno):
    print('name:{}'.format(name))
    print('age:{}'.format(age))
    print('mno:{}'.format(mno))
details(mno=6297496207,name="usha",age=24)

#nested function

def outer(*a):
    print("outer function",a)
    def inner():
        print("inner function")
    inner()
outer(1,2,3)

#passing list:
# 1)

def usha(a):
    for i in a:
        print(i)
usha([1,2,3,4])

# 2)
def usha(number):
    return number**2
print(usha(10))


#lambda function
# 1)

print((lambda number:number**2)(20))

# 2)

print((lambda a,b:a+b)(23,24))

# by using if else cond:

(lambda number:print('yes')if number%2==0 else print('no'))(20)


#lambda vs funtion
#function

# 1)
def iseven(number):
    if number%2==0:
        print("even")
    else:
        print("not even")
iseven(25)

# 2)
def square(number):
    return number**2
print(square(8))

#lambda function
#1)
(lambda number:print("even")if number%2==0 else print("not even"))(25)

# 2)
print((lambda number:number**2)(8))


#class and objects:

class SampleClass:
    attribute1=24
    attribute2=10
obj1=SampleClass()
obj2=SampleClass()
obj3=SampleClass()
print(obj1.attribute1)
print(obj2.attribute2)
print(obj3.attribute1)
print(obj1.attribute2)
print(obj2.attribute1)
print(obj3.attribute2)

#updating property of attribute

class SampleClass:
    attribute1=24
    attribute2=10
obj1=SampleClass()
obj2=SampleClass()

obj1.attribute1=100
print(obj1.attribute1)

# by using method

class SampleClass:
    def SampleMethod(self):
        print('this is method calling')

obj1=SampleClass()
obj1.SampleMethod()