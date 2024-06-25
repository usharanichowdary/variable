#clear

my_dict = {'name': 'usha', 'age': 25}
my_dict.clear()
print(my_dict) 

#copy
my_dict = {'name': 'usha', 'age': 25}
a= my_dict.copy()
print(a) 

#keys

keys = ('name', 'age', 'city')
b = dict.fromkeys(keys, 'unknown')
print(b) 


my_dict = {'name': 'Alice', 'age': 25}
print(my_dict.keys())  

#pop key

my_dict = {'name': 'Alice', 'age': 25}
age = my_dict.pop('age')
print(age)  
print(my_dict) 



#get

my_dict = {'name': 'Alice', 'age': 25}
print(my_dict.get('name'))  # Output: Alice
print(my_dict.get('city', 'Not Found'))  


#items

my_dict = {'name': 'Alice', 'age': 25}
print(my_dict.items())  

#values

my_dict = {'name': 'Alice', 'age': 25}
print(my_dict.values())  

#update

my_dict = {'name': 'Alice', 'age': 25}
my_dict.update({'age': 26, 'city': 'New York'})
print(my_dict)  

#set default

my_dict = {'name': 'Alice', 'age': 25}
city = my_dict.setdefault('city', 'New York')
print(city)  
print(my_dict)  


#by looping

my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

for key in my_dict:
    print(key)



# Iterating over values

my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

for value in my_dict.values():
    print(value)




# Iterating over key-value pairs

my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
for key, value in my_dict.items():
    print(f"{key}: {value}")



# modifying

my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
for key in my_dict:
    if key == 'age':
        my_dict[key] += 1

print(my_dict)  

# Combining two dictionaries

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

combined_dict = dict1.copy()  
for key, value in dict2.items():
    combined_dict[key] = value  
print(combined_dict)  

# Creating a list

my_list = [1, 2, 3, 4, 5]
print(my_list)  

#append

l= [1, 2, 3, 4, 5]
l.append("python")
print(l)

#slicing

l= [1, 2, 3, 4, 5]
print(l[2:4])

#extend

l= [1, 2, 3, 4, 5]
l.extend([6,7,8,"python"])
print(l)

# Removing elements

l= [1, 2, 3, 4, 5]
l.remove(3)
print(l)  

#pop

l=[1,24,
34,35,6,8]
l.pop(2)
print(l)

#count
l= [1, 2, 3, 4, 5]
print(l.count(1))

#index
l=[1,24,1,'true',0]
print(l.index('true'))

#insereting

l=[1,24,25,'usha']
l.insert(0,"xy")
print(l)

#looping of list

l= [1, 2, 3, 4, 5]
for i in l:
    print(i)


#iterate with index

l= [1, 2, 3, 4, 5]
for i in range(len(l)):
    print(f" {i}: {l[i]}")

#multiplying

l= [1, 2, 3, 4, 5]
for i in range(len(l)):
    l[i] *= 2
print(l) 

#squaring

l= [1, 2, 3, 4, 5]
s= [x**2 for x in l]
print(s)

#while looping

l= [1, 2, 3, 4, 5]
index = 0
while index < len(l):
    print(l[index])
    index += 1
