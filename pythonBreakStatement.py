from numpy.random import randint
#GENERATE 10 RANDOM INTERGERS NUMBERS IN RANGER FROM 1 TO 15


x16 = randint(1,15,10)
for i in x16:
    print(i)
    if i>10:
        break
print("The last value of i is:", i)
print(x16)