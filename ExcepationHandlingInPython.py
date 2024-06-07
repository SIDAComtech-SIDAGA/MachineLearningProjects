#An error that occurs while a program is running is called an exception.
#Thanks to the elements that we will just 
'''
try:
    <code_that_may_rise_an_exception>
except:
    <code_to_handle_the_exeception_if_it_occurs>
   '''

index = int(input("Enter the index"))

try:
    my_list = [1,2,3,4,5]
    print(my_list[index])
except:
    print("Enter a valid index")