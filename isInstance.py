i = 12
if isinstance(i,int):
    print("First instance")
    i += 1
elif isinstance(i,str):
    print("Second instance")
    i = int(i)
    i += 1
else:
    print("Hard to take")

print(i)