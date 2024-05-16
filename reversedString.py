a = 'hello'
result = (''.join(reversed('Sidaga')))
print(result)
print(list(result))


name = "Sidaga Waziri Kihongo"
print(list(name))
print(result.upper())

sid = "You"
it = iter(sid)
print(next(it))
print(next(it))
print(next(it))

a = reversed("My name")
print(a)
print(list(a))

# coverting iterator back to string 
a = reversed("My name")
print(a)
result = ''.join(a)
print(result)