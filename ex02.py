for i in range(10):
    print(i)
for i in range(5, 10):
    print(i)
print()
for i in range(1,10,2):
    print(i)

import time
print(dir(time))
dir()

for i in range(10):
    print(i)

li = [1]
print(li)
li.append(3)
print(li)

for i in li:
    print(i)

print(dir(li))


tu = (1,2)
print(type(tu))
print(len(tu))

tv = 3, 4
print(type(tv))

a, b = 1, 1
for i in range(10):
    print(a)
    a, b = b, a+b

di = {"name":"john", "age":19}
print(type(di))
print(di.keys())
print(di.values())
print(di.items())


se = {1,2,3,1,2,3}
print(type(se))
print(se)

b3 = {a for a in range(3, 1000, 3)}
b5 = {a for a in range(5, 1000, 5)}
bae = b3|b5
print(sum(bae))