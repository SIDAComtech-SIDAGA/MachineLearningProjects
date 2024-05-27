import numpy as np
import pandas as pd
# from matplotlib import pyplot as plt
X = np.random.random((10,3))
# Y = np.random.randint(10, size=10)
# dt = pd.DataFrame(Y)
# dt2 = pd.DataFrame(X)
# print("Data two")
# print(dt2)
# print("Data one dt")
# print(dt)
# print(Y)
# print(X)
Xmean = X.mean(0)
print(Xmean)
Xmean = X.mean()
print(Xmean)

#And now we can center the X array by substracting the mean(this is the broadcasting operation)

X_centered = X -Xmean
print("Centered Mean")
print(X_centered)
print("Double checking if we have done it correctly")
print(X_centered.mean(0))

print("Trying to generate random names")
# namesdt = np.random.choice(, size=20)
names = ["Sidaga", "Shein","Shude", "Dorcas", "Baraka"]
namesdt = np.random.choice(names, size=5)
print(namesdt)
nDT = pd.DataFrame(namesdt)
print(nDT)