import pandas as pd
import numpy as np

#use pandas to extract rainfall inches as a numpy array

# rainfall = pd.read_csv('data/Seattle2014.csv')['PRCP'].values
# inches = rainfall / 254 #1/10mm -> inches
# inches.shape

# COMPARISON OPERATORS AS UFUNCS 

# x = np.array([1,2,3,4,5])
# y = x < 3
# print(y.dtype)
# print(y)
# print(x + 2  )
# y2 = x > 3
# print(y2)
# print(x >= 3)
# print(x <= 3)

# print(x != 3)
# print(x == 3)
# print((2*x) == (x**2))

u = np.random.RandomState(0)
print(u)
x = u.randint(10, size=(3,2))
print(x)
print(x < 6)

# WORKING WITH BOOLEAN ARRAYS 

#counting enteries

print(np.count_nonzero(x < 6))
print(np.sum(x < 6))

#how many values less than 6 in each row?

print(np.sum(x < 6, axis=1))

#Are there any values greater than 8?
print(np.any(x > 6))

print(np.any(x < 0))


#are all values less than 10?
print(np.all(x < 10))
print(f"are all entries greater then 11 ",np.all(x > 11))

print(f"are all values equal to 6 ", np.all(x == 6))

#NP.ALL AND NP.ANY CAN BE USED ALONG THE PARTICULAR AXES AS WELL
print(np.all(x < 8, axis=1))

#np.sum((inches > 0.5) & (inches < 1))

