a = input("Enter the value of a")
b = input("Enter the value of b")

try:
    division = a / b
    print(division)
except Exception as err:
    print("Please enter a valid value. ", err)
    
else:
    print("Both values were valid")
finally:
    print("Finaly")
    
# We can aslo add a finally clause if we need to run code that should always run, even if an Exception is raised in try a