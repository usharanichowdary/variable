#__init__

class constructorclass:
    def __init__(self):
        print("this method was called automatically")
obj1=constructorclass()

class BanKAccount:
    def __init__(self,AccountNo,AccountName,Ifsecode,Balance):
        self.AccountNo= AccountNo
        self.AccountName=AccountName
        self.Ifsecode=Ifsecode
        self.Balance=Balance
    def details(self):
        print(self.AccountNo,self.AccountName,self.Ifsecode,self.Balance)
obj1=BanKAccount(1234555,'usha','Uno09798',10000)
obj1.details()
    
#check balance:

class BanKAccount:
    def __init__(self,AccountNo,AccountName,Ifsecode,Balance):
        self.AccountNo= AccountNo
        self.AccountName=AccountName
        self.Ifsecode=Ifsecode
        self.Balance=Balance
    def withdraw(self,amount):
        self.Balance-=amount
    def deposit(self,amount):
        self.Balance+=amount
    def checkBalance(self):
        print(self.Balance)
    
obj1=BanKAccount(1234555,'usha','Uno09798',10000)
print(obj1.AccountName)
obj1.checkBalance()
obj1.deposit(2000)
obj1.checkBalance()
obj1.withdraw(8000)
obj1.checkBalance()

#INHERITANCE
# 1)single inheritance

class parent:
    def method1(self):
        print("iam parent")
class child(parent):
    def method2(self):
        print("iam child")

obj1=child()
obj1.method1()
obj2=parent()
obj2.method2()

#2) multiple inheritance
class father:
    def method1(self):
        print("iam father")
class mother:
    def method2(self):
        print("iam mother")
class child(father,mother):
    def method3(self):
        print("iam child")

obj1=child()
obj1.method1()
obj1.method3()
obj1.method2()
obj2=mother()
obj2.method3()

# 3)multilevel inheritance

class grandfather:
    def method1(self):
        print("iam grandfather")
class father(grandfather):
    def method2(self):
        print("iam father")
class child(father):
    def method3(self):
        print("iam child")

obj1=child()
obj1.method1()
obj1.method2()
obj1.method3()
obj2=father()
obj2.method1()

# 4) hirerachical inheritance

class parent:
    def parentmethod(self):
        print("iam parent")
class child1(parent):
    def child1method(self):
        print("iam child1")
class child2(parent):
    def child2method(self):
        print("iam child2")

obj1=child1()
obj1.parentmethod()
obj1.child1method()
obj2=child2()
obj2.parentmethod()
obj2.child2method()


# hybrid inheritance
class grandparent:
    def grandparentmethod(self):
        print("iam grandparent")
class parent1(grandparent):
    def parent1method(self):
        print("iam parent")
class parent2:
    def parent2method(self):
        print("iam parent2")
class child(parent1,parent2):
    def childmethod(self):
        print("iam child")

obj1=child()
obj1.parent2method()
obj1.parent1method()
obj1.grandparentmethod()
obj1.childmethod()


#POLYMORPHISM

class A:
    def usha(self):
        print("this is class A")
class B:
    def usha(self):
        print("this is class B")
class C:
    def usha(self):
        print("this is class C")
def poly(obj):
    obj.usha()

obj1=A()
obj2=B()
obj3=C()

poly(obj1)
poly(obj2)
poly(obj3)

#Modules
def add(a,b):
    return a+b
def sub(a,b):
    return a-b

a=float(input("enter number 1: "))
b=float(input("enter number 2: "))
option=int(input('enter 1 for add or enter 2 for sub'))
if option==1:
    print(add(a,b))
elif option==2:
    print(sub(a,b))
else:
    print("you have choosen wrong option")

