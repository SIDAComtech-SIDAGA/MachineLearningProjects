file_name = input("Enter the file name")
split_f_name = file_name.split(".")
f_name = split_f_name[0]
e_name = split_f_name[-1]
print("File name is\t",f_name)
print("File extension \t",e_name)
# print(split_f_name)