print("Hello Sidaga, You gonna be fineee")
my_num = 5
print(my_num,type(my_num))

my_float = 2.5
my_string = "How you gonna be fineee?"
print(my_float,type(my_float), my_string, type(my_string))

set = {1,2,3,4,5,6,7,8}
x = 10
y = 5
print(x , y)

print(x is y)
print(x is not y)
print(x in set )
print(y in set)

# if else 
x2 = 10
if(x > 0):
    print("positive")
elif(x == 0):
    print("Zero")
else:
    print("Negative")
    
# while 
# x3 = 4
# x4 = 10
# while(x3<x4):
#     print("I am Sidaga Waziri Kihongo")
x ="I am Sidaga Waziri Kihongo"
for i in range(1,10):
    print(x)
    
i = 1
while i<=10:
    print(i)
    i += 1
my_list = [1,2,3,4,5]
for i in my_list:
    print('\t',i)
    
my_list2 = [1,2,3,4,5,6,6,7,8,9,10]

my_tuple = (1,2,3,4,5,6,7,8,9,10)

my_set = {1,2,2,3,4,5,5,6,6,77,8,8,8,0}
for i in my_set:
    print(i)
    
my_dictionary = {'name':'Waziri','age':30 ,'city':'Iringa'}
# nested dict 
nested_dict ={
    'person1': {'name':'Alice','age':30},
    'person2': {'name':'Sidaga', 'age': 23},
    'person3': {'name': 'Baraka','age':40}
}
for i in nested_dict.values():
    print(i)
    
# Difference form of creating a function 
def greet():
    print('Hello Sidaga')
greet()

def greet(name):
    print("Hello", name ," ! ")

greet("Sidaga") #Function call with the argument

#Function with the default parameters

def greet(name="Sidaga"):
    print("Hello", name)
greet()
greet("Shein")

#Function with the return value

def add(x,y):
    return x + y
result = add(3,6)
print("Result", result)

#Function with variable numbers
def add2(*args):
    sum = 0
    for num in args:
        sum += num
    return sum
result = add2(1,2,3,4,5,6,7,8)
print("Result", result)

# Function with keyword arguments 
def greeting(**kwargs):
    print("Hello", kwargs['name'])
greet(name = "Sidaga")

# Lambda function 
double = lambda x: x*2
print(double(12))


name = "My name is Sidaga Waziri Kihongo"
print(len(name))    
print(name.upper())
print(name.lower())
print("yoh",name.strip())
print(name.split())
print(name.replace('Sidaga','Shude'))
print(name.find('Sidaga Waziri'))
print(name.startswith('A'))

