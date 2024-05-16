#UNICODE STRING TYPE
s = 'hello'
print(type(s))

#A BYTE STRING 
b = b'hello'
print(type(b))

#CONVERTING STR TO BYTES

s = 'hello'
b = s.encode('utf-8')
print(type(b))

#DECODING FROM BYTES TO STRING

b = b'hello'
s = b.decode('utf-8')
print(s)
print(type(s))