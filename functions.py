def myFunction(myName, lName):
    print(myName + " " + lName)
    
myFunction("Sidaga","Shein")

#if you dint know how many arguments are going to be passed then you should use * before the parameter variable

def my_function(*kids):
    print("The youngest child is " + kids[3])
my_function("Sidaga", "Shein", "Baraka", "Shude", "Dorcas")

def my_funct(child3, child2, child1):
    print("The youngest child is" + child3)
my_funct(child3="Sidaga", child2="Shude", child1="Shein")
    

#Passing a list of arguments
def my_list_function(food):
    for x in food:
        print(x)
fruits = ["Apple", "Banana", "Cherry"]
my_list_function(fruits)

#Return values

def ret_value_function(x):
    return x * 5
print(ret_value_function(10))
print(ret_value_function(20))
print(ret_value_function(30))

#function defination can not be emppty but for some reason if you find sometime the function is empty then use pass

def my_em_function():
    pass

#You can specify that the function can have only positional arguments by adding "/" after the parameter

def postional_function(x,/):
    print(x)
postional_function(3)


#Recursive function

def tri_recursion(k):
    if(k>0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result
print("\n\nRecursion example Results")
tri_recursion(6)

my_tuple = (1,2,3)
tuple_hash = hash(my_tuple)
print(f"The hash value of the tuple{my_tuple} is {tuple_hash}")