x = 5

while x < 15:
    if x % 5 == 0:
        print("Even number found")
        break
    print(x)
    x += 2
    
else:
    print("All number were odd")