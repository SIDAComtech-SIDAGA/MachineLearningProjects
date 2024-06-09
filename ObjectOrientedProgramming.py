# In Object oriented Programming(OOP), we define classes that act as blueprints to create objects in Python with attributes and methods (functionally associated with the objects)
class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
#Creating an Instance

# To create sn intsnce of a dog, we need to specify the name and age of thee dog 

my_dog = Dog("Nora", 20)
print(my_dog.name, my_dog.age)
print("But my dog now is being called as Sidaga")

my_dog.name = "Sidaga"

print("Here is the new Name", my_dog.name)

del my_dog.name
print(len(my_dog.name))
my_dog.name = "Alfan"

print("I have deleted ", my_dog.name)