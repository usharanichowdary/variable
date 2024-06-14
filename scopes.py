#gobal scope

a=10
def encscope():
    print(a)
    def localscope():
        print(a)
    localscope()
encscope()

#enclosed scope

def encscope():
    a=20
    print(a)
    def localscope():
        print(a)
    localscope()
encscope()
print(a)

#local scope

def encscope():
    def localscope():
        a=30
        print(a)
    localscope()
    print(a)
encscope()
print(a)

def fun1():
    a=40
    def fun2():
        print(a)
        def fun3():
            print(a)
        fun3()
    fun2()
fun1()


#file handling
#Read mode

f=open('file.txt','r')
c=f.read()
print(c)
f.close()


#write mode
f=open('file.txt','w')
c=f.write('this is write mode')
print(c)
f.close()


#append

f=open('file.txt','a')
c=f.write('this is usha')
print(c)
f.close()


#readlines function

f=open('file.txt','r')
c=f.readlines(1)
print(c)
f.close()

#try and except
def a(a,b):
    return (a)
try:
    print(a)
except:
    print('error')
else:
    print('no error')
finally:
    print('completed')

# 2) 
def add(num1,num2):
    return(num1+num2)

print(add(1,2))
print(add(89,5))
print(add(12,'u'))
print(add(1,99))
print(add('execution','completed'))


# 3)
def add(num1,num2):
    try:
        return(num1+num2)
    except TypeError:
        return("invalid")
       

print(add(1,2))
print(add(89,5))
print(add(12,'u'))
print(add(1,99))
print(add('execution','completed'))

