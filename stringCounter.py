String_input = input("Enter the string")
# initializing the dictionary 
dict = {}

# using the for loop to iterate each character and i is the character in a string 
for i in String_input:
    # print(i)
    if i in dict:
        dict[i] += i
        print(dict[i])
    else:
        # if the character appear just once then print it once 
        dict[i] += i
        print(dict[i])
else:
    dict[i] = 1
    print(dict[i])
print(dict)