import numpy as np

a = np.array([0,1,2])
b = np.array([5,5,5])
# print(a + b)

###
# print(a + 5)

M = np.ones((3,3))
# print(M)
# print("\n")
# print(M + a)

c = np.arange(10)
print(c)

d = np.arange(10)[:, np.newaxis]
print(d)
print(c + d)

print("###Dimensionalism")

e = np.arange(3).reshape((3,1)) + np.arange(3)
print(e)

M = np.ones((2,3))
print(M.shape)
a = np.arange(3)
print(a.shape)
print("Broadcasting")
print(M + a)
print(a + M)

print("broadcasting 2")
a2 = a[:, np.newaxis].shape
print(a.shape)
print(a2)

print("Broadicasting rules apply to any binary ufunc")

sidaga = np.logaddexp(M,a)
print(sidaga)