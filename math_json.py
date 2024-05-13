q = abs(-7.12)
print(q)


w = pow(2,3)
print(w)

# THE MATH MODULE 

import math
e = math.sqrt(4)
print(e)

r = math.ceil(1.4)
t = math.floor(1.4)

print(r)
print(t)

a1 = math.ceil(1000)
a2 = math.floor(1000)

aa = math.pi
print(aa)

import json
xx = '{"name":"John","age":30,"city":"New York"}'
# Parse x
y = json.loads(xx)
# print the result is a python dictionary
print(y["age"])

# If you have a python object you can convert it into a JSON string by using json.dump()

xy = {
    "name": "John",
    "age": 30,
    "city": "New York"
} 

yy = json.dumps(xy)
print(yy[::])


print(json.dumps({"name": "John","age":30}))
print(json.dumps(["apple","banana"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("helloe"))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

dict = {
    "name": "Sidaga",
    "age": 22,
    "Married": False,
    "Divorces": False,
    "Children": ("Baraka", "Dorcas", "Shein"),
    "pets": ("Cat", "Dog"),
    "Cars":[
        {"Model": "BMW 230", "mpg": 27.5},
        {"Model": "Ford Edge", "mpg":24.1}
    ] 
}
print(dict.values())
print(json.dumps(dict,indent=4, sort_keys=True))