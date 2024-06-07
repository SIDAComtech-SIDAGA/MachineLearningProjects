#Zip() is an amazing built-in function that we use to 
#to iterate over multiple sequiences at once,
#Getting their corresponding elements in each eteration

my_List1 = [1,2,3,4]
my_List2 = [5,6,7,8]

for elem1, elem2 in zip(my_List1, my_List2):
    print(elem1,elem2)