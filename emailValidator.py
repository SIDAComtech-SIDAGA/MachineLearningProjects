Email_address = input('Input the email')
#  using split to split the email into parts 
split_email = Email_address.split(".")
print(split_email[-1])
#Giving variables to fundamentals and special characters

a = '@'
b = 'com'
c ='net'

# using if statement to know if the email is valid or not 
if a in split_email[0] and b or c in split_email[-1]:
    print("Valid Email")
else:
    print("Invalid email")