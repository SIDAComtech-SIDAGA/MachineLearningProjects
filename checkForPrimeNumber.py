num = int(input("Enter a number :"))
if num < 1:
    print(num, "Is not a prime number ")
else:
    for i in range(2,num):
        if num % i == 0:
            print("not a prime number")
            break
    else:
        print("It is a prime number")