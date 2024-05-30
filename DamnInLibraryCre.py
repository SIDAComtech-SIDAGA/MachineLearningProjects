#FANCY INDEXING
import numpy as np
rand = np.random.RandomState(42)
x =rand.randint(100, size=10)
print(rand)
print(x)
# rand = np.random.randint(100, size=10)
# print(rand)

#Suppose we want to access three different elements. We could do it like this:

print(x[3],x[7], x[2])

#ALtenatively we can pass a single list or array of indeces to obtain the same result

ind = [3,7,4]
print(x[ind])

ind2 = np.array([
    [3,7],
    [4,5]
])
print(x[ind2])

#Fancyb indexing also works in different/multiple dimensions. Consider the following
X = np.arange(12).reshape((3,4))
print(X)

print("\t")
row = np.array([0,1,2])
col = np.array([2,1,3])

print(X[row,col])

print(row[:, np.newaxis], col)


# COMBINED INDEXING 

# For even more powerful operation, fany indexing can be combined with other indexinf schems we've seen 
print("Combined indexing")
print(X)
print("Lets COmbines")
print(X[2,[2,0,1]])
print("We can also combine fancy indxinf with slicing")
print(X[1:,[2,0,1]])

print("And we can combine fancy indexing with masking")
mask = np.array([1,0,1,0], dtype=bool)
print(X[row[:,np.newaxis],mask])
