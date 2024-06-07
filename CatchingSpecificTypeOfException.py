'''
try:
    <code_that_May_rise_an_eeror>
except:
    <code_to_handle_an_exception>'''
    
index = int(input("Enter an Index"))
try:
    my_list = [1,2,3,4,5]
    print(my_list[index])
except IndexError:
    print("Please enter a valid index")
    
    
#Assigning name to an exception

index = int(input("Enter the index"))
try:
    my_list = [1,2,3,4,5]
    print(my_list[index])
except IndexError as e:
    print("Exception raised :", e)
    