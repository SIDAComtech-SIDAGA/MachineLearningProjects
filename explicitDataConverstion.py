#Converting between datatype

a = '123'
b = int(a)
print(b)

#COnverting float

a = '123.456'
b = float(a)
c = int(b)
d = int(c)
print(a,b,c,d)

#You can also convert sequence or collection type
a = 'hello'
print(list(a))
print(tuple(a))
print(set(a))