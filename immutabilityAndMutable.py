#An object is called mutable if it can be changed. For example, when you pass a list to some function the list can change
m = [1,2,3,4,5]

def f(m):
    m.append(9)
f(m)
print(m)
m.append(12)
print(m)